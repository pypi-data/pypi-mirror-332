# SPDX-FileCopyrightText: 2025 Tjark Sievers
#
# SPDX-License-Identifier: MIT

"""
TRIQS interface to **EDIpack** exact diagonalization solver.
"""

import os
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from warnings import warn

import numpy as np
import triqs.operators as op
from edipy2 import global_env as ed
from mpi4py import MPI
from triqs.gf import BlockGf, Gf, MeshImFreq, MeshReFreq

from .bath import Bath, BathGeneral, BathHybrid, BathNormal
from .fit import BathFittingParams, _chi2_fit_bath
from .hamiltonian import parse_hamiltonian
from .util import IndicesType, chdircontext, validate_fops_up_dn, write_config


class EDIpackSolver:
    """
    This class represents the **EDIpack** exact diagonalization library and
    incapsulates its internal state. Its methods and attributes allow to perform
    ED calculations and to access their results.

    .. note::

        At most one instance of this type can exists at any time. An attempt to
        create more such objects will raise an :py:class:`AssertionError`.
    """

    # EDIpack maintains the state of a simulation as a set of global variables.
    # Therefore, this state must be controlled by at most one EDIpackSolver
    # instance at any time.
    instance_count = [0]

    # Default configuration
    default_config = {
        # DMFT
        "NLOOP": 0,
        "DMFT_ERROR": 0.0,
        "NSUCCESS": 0,
        # Hartree-Fock
        "HFMODE": False,
        "XMU": 0.0,
        # Phonons
        "PH_TYPE": 1,
        "NPH": 0,
        # Fixed density calculations
        "NREAD": 0.0,
        "NERR": 0.0,
        "NDELTA": 0.0,
        "NCOEFF": 0.0,
        # ED
        "ED_PRINT_SIGMA": False,
        "ED_PRINT_G": False,
        "ED_PRINT_G0": False,
        "RDM_FLAG": False,
        "ED_FINITE_TEMP": True,
        "ED_TWIN": False,
        "ED_SECTORS": False,
        "ED_SECTORS_SHIFT": 0,
        "ED_SOLVE_OFFDIAG_GF": False,  # TODO
        "ED_ALL_G": True,
        "ED_OFFSET_BATH": 0.0,
        # TODO: Susceptibilities
        "LTAU": 1000,  # TODO: To be set in solve()
        "CHISPIN_FLAG": False,  # TODO: To be set in __init__()
        "CHIDENS_FLAG": False,  # TODO: To be set in __init__()
        "CHIPAIR_FLAG": False,  # TODO: To be set in __init__()
        "CHIEXCT_FLAG": False,  # TODO: To be set in __init__()
    }

    def __init__(
        self,
        hamiltonian: op.Operator,
        fops_imp_up: list[IndicesType],
        fops_imp_dn: list[IndicesType],
        fops_bath_up: list[IndicesType],
        fops_bath_dn: list[IndicesType],
        **kwargs,
    ):
        r"""
        Initialize internal state of the underlying **EDIpack** solver.

        The fundamental operator sets (**fops** for short) define sizes of
        impurity and bath Hilbert spaces. The expected **fops** objects are
        lists of tuples (pairs). Each element ``(b, i)`` of such a list
        corresponds to a single fermionic degree of freedom created by
        the many-body operator ``c_dag(b, i)``. ``b`` and ``i`` are a (string or
        integer) block index and an index within a block respectively, which
        are used to construct output :py:class:`Green's function
        containers <triqs.gf.block_gf.BlockGf>`.

        :param hamiltonian: Many-body electronic Hamiltonian to diagonalize.
            Symmetries of this Hamiltonian are automatically analyzed and
            dictate the choice of **EDIpacks**'s
            :f:var:`ED mode <f/ed_input_vars/ed_mode>` and
            :f:mod:`bath geometry <f/ed_bath>`. This choice
            remains unchangeable throughout object's lifetime.
        :type triqs.operators.operators.Operator:

        :param fops_imp_up: Fundamental operator set for spin-up impurity
            degrees of freedom.
        :type fops_imp_up: list[tuple[int | str, int | str]]

        :param fops_imp_dn: Fundamental operator set for spin-down impurity
            degrees of freedom.
        :type fops_imp_dn: list[tuple[int | str, int | str]]

        :param fops_bath_up: Fundamental operator set for spin-up bath
            degrees of freedom.
        :type fops_bath_up: list[tuple[int | str, int | str]]

        :param fops_bath_dn: Fundamental operator set for spin-down bath
            degrees of freedom.
        :type fops_bath_dn: list[tuple[int | str, int | str]]

        :param input_file: Path to a custom input file compatible with
            **EDIpack**'s :f:func:`f/ed_input_vars/ed_read_input`.
            When specified, it is used to initialize **EDIpack**.
            This option is mutually exclusive with all other keyword arguments.
        :type input_file: str, optional

        :param verbose: Verbosity level of the solver: 0 for almost no output,
            5 for the full output from **EDIpack**.
        :type verbose: int, default=3

        :param cutoff: Spectrum cutoff used to determine the number of states
                       to be retained.
        :type cutoff: float, default=1e-9

        :param gs_threshold: Energy threshold for ground state degeneracy loop.
        :type gs_threshold: float, default=1e-9

        :param ed_sparse_h: Switch between storing the sparse matrix
            :math:`\hat H` (*True*) and direct on-the-fly evaluation of
            the product :math:`\hat H |v\rangle` (*False*).
        :type ed_sparse_h: bool, default=True

        :param ed_total_ud: Force use of the total spin-up and spin-down
            occupancies as quantum numbers instead of the orbital-resolved
            occupancies.
        :type ed_total_ud: bool, default=False

        :param lanc_method: Select the method to be used in
            the determination of the spectrum, one of *"arpack"*, *"lanczos"*
            (simple Lanczos method, only works at zero temperature, can be
            useful in some rare cases, when ARPACK fails) and *"dvdson"*
            (no-MPI mode only).
        :type lanc_method: str, default="arpack"

        :param lanc_nstates_sector: Initial number of states per sector
            to be determined.
        :type lanc_nstates_sector: int, default=2

        :param lanc_nstates_total: Initial total number of states
            to be determined.
        :type lanc_nstates_total: int, default=2

        :param lanc_nstates_step: Number of states added to the spectrum
            at each step.
        :type lanc_nstates_step: int, default=2

        :param lanc_ncv_factor: Set the size of the block used in
            Lanczos-ARPACK by multiplying the required Neigen
            (``NCV = lanc_ncv_factor * Neigen + lanc_ncv_add``).
        :type lanc_ncv_factor: int, default=10

        :param lanc_ncv_add: Adds up to the size of the block to prevent it
            from becoming too small
            (``NCV = lanc_ncv_factor * Neigen + lanc_ncv_add``).
        :type lanc_ncv_add: int, default=0

        :param lanc_niter: Number of Lanczos iterations in spectrum
            determination.
        :type lanc_niter: int, default=512

        :param lanc_ngfiter: Number of Lanczos iterations in GF determination
            (number of momenta).
        :type lanc_ngfiter: int, default=200

        :param lanc_tolerance: Tolerance for the Lanczos iterations as used
            in ARPACK.
        :type lanc_tolerance: float, default=1e-18

        :param lanc_dim_threshold: Minimal dimension threshold to use Lanczos
            determination of the spectrum rather than LAPACK-based
            exact diagonalization.
        :type lanc_dim_threshold: int, default=1024

        :param bath_fitting_params: Parameters used to perform bath fitting.
        :type bath_fitting_params: BathFittingParams, optional
        """
        assert (
            self.instance_count[0] < 1
        ), "Only one instance of EDIpackSolver can exist at any time"

        validate_fops_up_dn(fops_imp_up, fops_imp_dn, "fops_imp_up", "fops_imp_dn")
        validate_fops_up_dn(fops_bath_up, fops_bath_dn, "fops_bath_up", "fops_bath_dn")

        self.norb = len(fops_imp_up)
        assert self.norb <= 5, f"At most 5 orbitals are allowed, got {self.norb}"

        self.fops_imp_up = fops_imp_up
        self.fops_imp_dn = fops_imp_dn
        self.fops_bath_up = fops_bath_up
        self.fops_bath_dn = fops_bath_dn

        # Detect GF block names
        block_names_up = [ind[0] for ind in fops_imp_up]
        block_names_dn = [ind[0] for ind in fops_imp_dn]
        if any(bn != block_names_up[0] for bn in block_names_up):
            warn(f"Inconsistent block names in {block_names_up}")
        if any(bn != block_names_dn[0] for bn in block_names_dn):
            warn(f"Inconsistent block names in {block_names_dn}")

        self.h_params = parse_hamiltonian(
            hamiltonian, self.fops_imp_up, self.fops_imp_dn, self.fops_bath_up, self.fops_bath_dn
        )
        self.nspin = self.h_params.Hloc.shape[0]

        if "input_file" in kwargs:
            self.input_file = Path(kwargs.pop("input_file"))
            self.input_file = self.input_file.resolve(strict=True)

            if kwargs:
                raise ValueError("'input_file' is mutually exclusive with other parameters")
        else:
            self.input_file = None

            c = self.default_config.copy()
            c["ED_VERBOSE"] = kwargs.get("verbose", 3)
            c["CUTOFF"] = kwargs.get("cutoff", 1e-9)
            c["GS_THRESHOLD"] = kwargs.get("gs_threshold", 1e-9)
            c["ED_SPARSE_H"] = kwargs.get("ed_sparse_h", True)
            c["LANC_METHOD"] = kwargs.get("lanc_method", "arpack")
            c["LANC_NSTATES_SECTOR"] = kwargs.get("lanc_nstates_sector", 2)
            c["LANC_NSTATES_TOTAL"] = kwargs.get("lanc_nstates_total", 2)
            c["LANC_NSTATES_STEP"] = kwargs.get("lanc_nstates_step", 2)
            c["LANC_NCV_FACTOR"] = kwargs.get("lanc_ncv_factor", 10)
            c["LANC_NCV_ADD"] = kwargs.get("lanc_ncv_add", 0)
            c["LANC_NITER"] = kwargs.get("lanc_niter", 512)
            c["LANC_NGFITER"] = kwargs.get("lanc_ngfiter", 200)
            c["LANC_TOLERANCE"] = kwargs.get("lanc_tolerance", 1e-18)
            c["LANC_DIM_THRESHOLD"] = kwargs.get("lanc_dim_threshold", 1024)

            # Impurity structure
            c["ED_MODE"] = self.h_params.ed_mode
            c["NSPIN"] = self.nspin
            c["NORB"] = self.norb

            # Bath geometry
            c["BATH_TYPE"] = self.h_params.bath.name
            c["NBATH"] = self.h_params.bath.nbath

            # Interaction parameters
            c["ULOC"] = self.h_params.Uloc
            c["UST"] = self.h_params.Ust
            c["JH"] = self.h_params.Jh
            c["JX"] = self.h_params.Jx
            c["JP"] = self.h_params.Jp

            # ed_total_ud
            ed_total_ud = kwargs.get("ed_total_ud", False)
            if isinstance(self.h_params.bath, BathNormal):
                c["ED_TOTAL_UD"] = ed_total_ud or (
                    not (self.h_params.Jx == 0 and self.h_params.Jp == 0)
                )
            elif isinstance(self.h_params.bath, (BathHybrid, BathGeneral)):
                c["ED_TOTAL_UD"] = True
            else:
                raise RuntimeError("Unrecognized bath type")

            # Bath fitting
            bfp = kwargs.get("bath_fitting_params", BathFittingParams())
            c.update(bfp.__dict__())

            self.config = c

        self.comm = MPI.COMM_WORLD

        # A temporary directory for EDIpack is created and managed by the MPI
        # process with rank 0. The directory is assumed to be accessible to all
        # other MPI processes under the same name via a common file system.
        if self.comm.Get_rank() == 0:
            self.workdir = TemporaryDirectory(prefix="edipack-", suffix=".tmp", dir=os.getcwd())
            self.wdname = self.workdir.name
        else:
            self.wdname = None
        self.wdname = self.comm.bcast(self.wdname)

        with chdircontext(self.wdname):
            if self.comm.Get_rank() == 0:
                if self.input_file is None:
                    self.input_file = Path("input.conf").resolve()
                    with open(self.input_file, "w") as config_file:
                        write_config(config_file, self.config)

                else:
                    Path("input.conf").symlink_to(self.input_file)

            self.comm.barrier()
            ed.read_input("input.conf")

            if self.comm.Get_rank() == 0:
                self.scifor_version = re.match(
                    r"^SCIFOR VERSION \(GIT\): (.*)", open("scifor_version.inc").readline()
                )[1]

                self.edipack_version = re.match(
                    r"^code VERSION: (.*)", open("code_version.inc").readline()
                )[1]
            else:
                self.scifor_version = ""
                self.edipack_version = ""

            self.scifor_version = self.comm.bcast(self.scifor_version)
            self.edipack_version = self.comm.bcast(self.edipack_version)

        if isinstance(self.h_params.bath, BathGeneral):
            ed.set_hgeneral(self.h_params.bath.hvec, self.h_params.bath.lambdavec)
        else:
            assert self.h_params.bath.data.size == ed.get_bath_dimension()

        # Initialize EDIpack
        ed.init_solver(bath=np.zeros(self.h_params.bath.data.size, dtype=float))

        # GF block names
        if ed.get_ed_mode() in (1, 2):  # normal or superc
            self.gf_block_names = (block_names_up[0], block_names_dn[0])
        else:
            self.gf_block_names = (block_names_up[0],)

        if ed.get_ed_mode() == 2:  # superc
            self.gf_an_block_names = (block_names_up[0] + "_" + block_names_dn[0],)

        self.instance_count[0] += 1
        self.comm.barrier()

    def __del__(self):
        self.comm.barrier()
        try:
            ed.finalize_solver()
            self.instance_count[0] -= 1
        # ed.finalize_solver() can fail if this __del__() method is called as
        # part of interpreter destruction procedure.
        except TypeError:
            pass

    @property
    def hloc(self) -> np.ndarray:
        r"""
        Read-only access to the matrix of the local impurity Hamiltonian
        :math:`\hat H_\text{loc}`.
        """
        return self.h_params.Hloc

    @property
    def Uloc(self) -> np.ndarray:
        r"""
        Local intra-orbital interaction :math:`U_\text{loc}`, one value
        per orbital, up to 5 values.
        """
        return ed.Uloc[: self.norb]

    @Uloc.setter
    def Uloc(self, values):
        assert len(values) == self.norb, f"Required exactly {self.norb} values"
        ed.Uloc = np.pad(values, (0, 5 - len(values)))

    @property
    def Ust(self) -> float:
        r"""Local inter-orbital interaction :math:`U_\text{st}`."""
        return ed.Ust

    @Ust.setter
    def Ust(self, value):
        ed.Ust = value

    @property
    def Jh(self) -> float:
        r"""Hund's coupling :math:`J_h`."""
        return ed.Jh

    @Jh.setter
    def Jh(self, value):
        ed.Jh = value

    @property
    def Jx(self) -> float:
        r"""Spin-exchange coupling :math:`J_x`."""
        return ed.Jx

    @Jx.setter
    def Jx(self, value) -> float:
        if (not ed.ed_total_ud) and (value != 0):
            raise RuntimeError("Cannot set Jx to a non-zero value")
        ed.Jx = value

    @property
    def Jp(self) -> float:
        r"""Pair-hopping coupling :math:`J_p`."""
        return ed.Jp

    @Jp.setter
    def Jp(self, value):
        if (not ed.ed_total_ud) and (value != 0):
            raise RuntimeError("Cannot set Jp to a non-zero value")
        ed.Jp = value

    @property
    def bath(self) -> Bath:
        r"""
        Access to the current :py:class:`bath <edipack2triqs.bath.Bath>` object
        stored in the solver. It is possible to assign a new bath object as long
        as it has the matching type and describes a bath of the same geometry.
        """
        return self.h_params.bath

    @bath.setter
    def bath(self, new_bath: Bath):
        """Set the bath object"""
        self.h_params.bath.assert_compatible(new_bath)
        self.h_params.bath = new_bath

    def solve(
        self,
        beta: float,
        *,
        n_iw: int = 4096,
        energy_window: tuple[float, float] = (-5.0, 5.0),
        n_w: int = 5000,
        broadening: float = 0.01,
    ):
        r"""
        Solve the impurity problem and calculate the observables, Green's
        function and self-energy.

        :param beta:
            Inverse temperature :math:`\beta = 1 / (k_B T)` for observable and
            Green's function calculations.
        :type beta: float

        :param n_iw: Number of Matsubara frequencies for impurity GF
            calculations.
        :type n_iw: int, default=4096

        :param energy_window: Energy window for real-frequency impurity GF
            calculations.
        :type energy_window: tuple[float, float], default=(-5.0, 5.0)

        :param n_w: Number of real-frequency points for impurity GF
            calculations.
        :type n_w: int, default=5000

        :param broadening: Broadening (imaginary shift away from the
            real-frequency axis) for real-frequency impurity GF calculations.
        :type broadening: float, default=0.01
        """
        # Pass parameters to EDIpack
        ed.beta = beta
        ed.Lmats = n_iw
        ed.wini, ed.wfin = energy_window
        ed.Lreal = n_w
        ed.eps = broadening

        # Solve!
        self.comm.barrier()
        with chdircontext(self.wdname):
            ed.set_hloc(hloc=self.h_params.Hloc)
            ed.solve(self.h_params.bath.data)
        self.comm.barrier()

    @property
    def e_pot(self) -> float:
        """Potential energy from interaction."""
        return ed.get_eimp(ikind=0)

    @property
    def e_kin(self) -> float:
        """Kinetic energy."""
        return ed.get_eimp(ikind=3)

    @property
    def densities(self) -> np.ndarray:
        """Impurity occupations, one element per orbital."""
        return ed.get_dens()

    @property
    def double_occ(self) -> np.ndarray:
        """Impurity double occupancy, one element per orbital."""
        return ed.get_docc()

    @property
    def superconductive_phi(self) -> np.ndarray:
        r"""Impurity superconductive :math:`\phi`-matrix in orbital space."""
        return ed.get_phi()

    @property
    def magnetization(self) -> np.ndarray:
        """
        Cartesian components of impurity magnetization vectors,
        one row per orbital.
        """
        return ed.get_mag().T

    def _make_gf(self, ed_func, real_freq, anomalous) -> BlockGf:
        if anomalous:
            if ed.get_ed_mode() != 2:  # superc
                raise RuntimeError("anomalous = True is only supported for " "superconducting bath")

        if real_freq:
            mesh = MeshReFreq(window=(ed.wini, ed.wfin), n_w=ed.Lreal)
            z_vals = [complex(z) + ed.eps * 1j for z in mesh]
        else:
            mesh = MeshImFreq(beta=ed.beta, S="Fermion", n_iw=ed.Lmats)
            z_vals = [complex(z) for z in mesh]

        with chdircontext(self.wdname):
            data = ed_func(z_vals, typ="a" if anomalous else "n")

        if anomalous:
            F = Gf(mesh=mesh, target_shape=(self.norb, self.norb))
            F.data[:] = np.rollaxis(data[0, 0, :, :, :], 2)
            return BlockGf(name_list=self.gf_an_block_names, block_list=[F], make_copies=False)

        if ed.get_ed_mode() in (1, 2):  # 2 spin blocks
            blocks = [Gf(mesh=mesh, target_shape=(self.norb, self.norb)) for _ in range(2)]
            # Block up
            blocks[0].data[:] = np.rollaxis(data[0, 0, :, :, :], 2)
            # Block down
            if self.nspin == 1:
                blocks[1].data[:] = blocks[0].data
            else:
                blocks[1].data[:] = np.rollaxis(data[1, 1, :, :, :], 2)
        else:  # One block
            blocks = [Gf(mesh=mesh, target_shape=(2 * self.norb, 2 * self.norb))]
            blocks[0].data[:] = np.transpose(data, (4, 0, 2, 1, 3)).reshape(
                len(mesh), 2 * self.norb, 2 * self.norb
            )

        return BlockGf(name_list=self.gf_block_names, block_list=blocks, make_copies=False)

    #
    # GF and self-energy properties
    #

    @property
    def g_iw(self) -> BlockGf:
        """Matsubara impurity Green's function."""
        return self._make_gf(ed.build_gimp, False, False)

    @property
    def g_an_iw(self) -> BlockGf:
        """Anomalous Matsubara impurity Green's function."""
        return self._make_gf(ed.build_gimp, False, True)

    @property
    def Sigma_iw(self) -> BlockGf:
        """Matsubara impurity self-energy."""
        return self._make_gf(ed.build_sigma, False, False)

    @property
    def Sigma_an_iw(self) -> BlockGf:
        """Anomalous Matsubara impurity self-energy."""
        return self._make_gf(ed.build_sigma, False, True)

    @property
    def g_w(self) -> BlockGf:
        """Real-frequency impurity Green's function."""
        return self._make_gf(ed.build_gimp, True, False)

    @property
    def g_an_w(self) -> BlockGf:
        """Anomalous real-frequency impurity Green's function."""
        return self._make_gf(ed.build_gimp, True, True)

    @property
    def Sigma_w(self) -> BlockGf:
        """Real-frequency impurity self-energy."""
        return self._make_gf(ed.build_sigma, True, False)

    @property
    def Sigma_an_w(self) -> BlockGf:
        """Anomalous real-frequency impurity self-energy."""
        return self._make_gf(ed.build_sigma, True, True)

    # Bath fitting
    chi2_fit_bath = _chi2_fit_bath
