# SPDX-FileCopyrightText: 2025 Tjark Sievers
#
# SPDX-License-Identifier: MIT

"""
Bath fitting tools.
"""

from copy import deepcopy
from dataclasses import dataclass

import numpy as np
from edipy2 import global_env as ed
from triqs.gf import BlockGf, MeshImFreq

from .util import chdircontext


@dataclass(frozen=True, kw_only=True)
class BathFittingParams:
    """Parameters of bath fitting."""

    scheme: str = "weiss"
    """
    Fitting scheme: *"delta"* to fit the hybridization function, *"weiss"* to
    fit the Weiss field.
    """
    # Minimization routine type: CGnr, minimize
    method: str = "minimize"
    """
    Minimization routine to use: *"CGnr"* for an algorithm from Numerical
    Recipes, *"minimize"* for an older FORTRAN 77 minimization procedure.
    """
    grad: str = "numeric"
    """
    Gradient evaluation method, either *"analytic"* or *"numeric"*.
    """
    tol: float = 1e-5
    """
    Tolerance level for the conjugate gradient method.
    """
    stop: str = "both"
    """
    Stopping condition for the conjugate gradient method.

        - *"target"*: :math:`|F_{n-1} - F_n| < tol (1+F_n)`.
        - *"vars"*: :math:`||x_{n-1} - x_n|| < tol (1+||x_n||)`.
        - *"both"*: Both conditions are fulfilled.
    """
    niter: int = 500
    """
    Maximal number of iterations.
    """
    n_iw: int = 1000
    """
    The number of Matsubara frequencies used in the fit.
    """
    weight: str = "1"
    r"""
    Weight function for the conjugate gradient minimization.

        - *"1"*: :math:`1`
        - *"1/n"*: :math:`1/n`, where :math:`n` is a Matsubara frequency number.
        - *"1/w_n"*: :math:`1/\omega_n`, where :math:`\omega_n` is a Matsubara
          frequency.
    """
    norm: str = "elemental"
    r"""
    Matrix norm to use in optimization, either *"elemental"* (sum of
    :math:`\chi^2`-norms for each matrix element) or *"frobenius"*.
    """
    pow: int = 2
    r"""
    Fit power for the calculation of the generalized distance as
    :math:`|G_0 - G_{0,\text{and}}| ^ \text{pow}`.
    """
    minimize_ver: bool = False
    """
    Use the old/Krauth (*False*) or the new/Lichtenstein (*True*) version of the
    minimization conjugate gradient procedure. Only relevant for
    *method="minimize"*.
    """
    minimize_hh: float = 1e-4
    """
    An unknown parameter used in the conjugate gradient minimization procedure.
    """

    def __dict__(self):
        assert self.scheme in ("delta", "weiss"), "Invalid value of 'scheme'"
        assert self.method in ("CGnr", "minimize"), "Invalid value of 'method'"
        assert self.grad in ("analytic", "numeric"), "Invalid value of 'grad'"
        assert self.tol >= 0, "'tol' cannot be negative"
        assert self.stop in ("target", "vars", "both"), "Invalid value of 'stop'"
        assert self.niter > 0, "'niter' must be positive"
        assert self.n_iw > 0, "'n_iw' must be positive"
        assert self.weight in ("1", "1/n", "1/w_n"), "Invalid value of 'weight'"
        assert self.norm in ("elemental", "frobenius"), "Invalid value of 'norm'"
        assert self.pow > 0, "'pow' must be positive"

        return {
            "CG_SCHEME": self.scheme,
            "CG_METHOD": {"CGnr": 0, "minimize": 1}[self.method],
            "CG_GRAD": {"analytic": 0, "numeric": 1}[self.grad],
            "CG_FTOL": self.tol,
            "CG_STOP": {"target": 1, "vars": 2, "both": 0}[self.stop],
            "CG_NITER": self.niter,
            "CG_WEIGHT": {"1": 1, "1/n": 2, "1/w_n": 3}[self.weight],
            "CG_NORM": self.norm,
            "CG_POW": self.pow,
            "CG_MINIMIZE_VER": self.minimize_ver,
            "CG_MINIMIZE_HH": self.minimize_hh,
            "LFIT": self.n_iw,
        }


def _chi2_fit_bath(self, g: BlockGf, f: BlockGf | None = None):
    """
    Perform bath parameter fit of a given Green's function.

    :param g: Normal component of the function to fit (either the hybridization
              function or the Weiss field).
    :type g: triqs.gf.block_gf.BlockGf

    :param f: Anomalous component of the function to fit (either the
              hybridization function or the Weiss field). Required iff the bath
              is superconducting.
    :type g: triqs.gf.block_gf.BlockGf

    :return: - A bath object that contains resulting parameters of the fit.
             - The normal component of the fitted function.
             - (*optional*) The anomalous component of the fitted function.

    :rtype: tuple[Bath, triqs.gf.block_gf.BlockGf] or
            tuple[Bath, triqs.gf.block_gf.BlockGf, triqs.gf.block_gf.BlockGf]
    """
    if (ed.get_ed_mode() == 2) != (f is not None):
        raise RuntimeError("The anomalous GF is required iff the bath is superconducting")

    fitted_bath = deepcopy(self.h_params.bath)

    def extract_triqs_data(d):
        return np.transpose(d[ed.Lmats :, ...], (1, 2, 0))

    with chdircontext(self.wdname):
        if ed.get_ed_mode() == 1:  # Normal, here nspin is important
            assert set(g.indices) == set(self.gf_block_names), "Unexpected block structure of g"

            func_up = extract_triqs_data(g[self.gf_block_names[0]].data)
            fitted_bath.data[:] = ed.chi2_fitgf(func_up, fitted_bath.data, ispin=0)
            if ed.Nspin != 1:
                func_dn = extract_triqs_data(g[self.gf_block_names[1]].data)
                fitted_bath.data[:] = ed.chi2_fitgf(func_dn, fitted_bath.data, ispin=1)

        elif ed.get_ed_mode() == 2:  # superc, here nspin is 1
            func_up = extract_triqs_data(g[self.gf_block_names[0]].data)
            func_an = extract_triqs_data(f[self.gf_an_block_names[0]].data)
            fitted_bath.data[:] = ed.chi2_fitgf(func_up, func_an, fitted_bath.data)

        elif ed.get_ed_mode() == 3:  # nonsu2, here nspin is 2
            func = extract_triqs_data(g[self.gf_block_names[0]].data)
            fitted_bath.data[:] = ed.chi2_fitgf(func, fitted_bath.data)

        else:
            raise RuntimeError("Unrecognized ED mode")

    #
    # Create fitted G0 or \Delta
    #

    mesh = MeshImFreq(beta=ed.beta, S="Fermion", n_iw=ed.Lmats)
    z_vals = np.array([complex(z) for z in mesh])
    get_method = ed.get_g0and if (self.config["CG_SCHEME"] == "weiss") else ed.get_delta
    g_out = g.copy()

    def pack_triqs_data(d):
        return np.transpose(d, (2, 0, 1))

    with chdircontext(self.wdname):
        if ed.get_ed_mode() == 1:  # normal
            out = get_method(z_vals, fitted_bath.data, ishape=5, typ="n")
            g_out[self.gf_block_names[0]].data[:] = pack_triqs_data(out[0, 0, ...])
            g_out[self.gf_block_names[1]].data[:] = pack_triqs_data(
                out[0, 0, ...] if (self.nspin == 1) else out[1, 1, ...]
            )
            return fitted_bath, g_out

        elif ed.get_ed_mode() == 2:  # superc
            out = get_method(z_vals, fitted_bath.data, ishape=5, typ="n")
            for bn in self.gf_block_names:
                g_out[bn].data[:] = pack_triqs_data(out[0, 0, ...])
            out_an = get_method(z_vals, fitted_bath.data, ishape=5, typ="a")
            f_out = f.copy()
            f_out[self.gf_an_block_names[0]].data[:] = pack_triqs_data(out_an[0, 0, ...])
            return fitted_bath, g_out, f_out

        else:  # nonsu2
            out = get_method(z_vals, fitted_bath.data, ishape=3)
            g_out[self.gf_block_names[0]].data[:] = pack_triqs_data(out)
            return fitted_bath, g_out
