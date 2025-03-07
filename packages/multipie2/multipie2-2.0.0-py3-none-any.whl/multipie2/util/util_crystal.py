"""
For crystal (for sympy element).
"""

import numpy as np
import sympy as sp

from multipie2.data.data_crystal import P_dict, t_dict
from multipie2.util.util import str_to_sympy

P_dict = {lattice: str_to_sympy(m) for lattice, m in P_dict.items()}
Pi_dict = {lattice: np.array(sp.Matrix(m).inv()) for lattice, m in P_dict.items()}
t_dict = {lattice: None if t is None else str_to_sympy(t) for lattice, t in t_dict.items()}

TOL_SAME_SITE = 1e-8
DIGIT = 8


# ==================================================
def shift_site(site):
    """
    Shift site within home unit cell.

    Args:
        site (ndarray): (set of) site (sympy or float).

    Returns:
        - (ndarray) -- shifted site.

    Note:
        - When using sympy elements, ensure that all elements are sympy. Creating an array like np.array([0, sp.S(1)/2, 1]) can be dangerous, as all elements may be treated as integers in some cases. To ensure that all elements are treated as sympy objects, it is recommended to use str_to_sympy.
    """
    site = np.mod(site, 1)
    site = np.vectorize(lambda i: i.args[0] if isinstance(i, sp.Mod) else i)(site)
    if site.dtype != object:
        site[np.abs(site - 1) < TOL_SAME_SITE] = 0
    return site


# ==================================================
def shift_bond(bond):
    """
    Shift bond within home unit cell.

    Args:
        bond (ndarray): (set of) bond (sympy or float) [vector+center].

    Returns:
        - (ndarray) -- shifted bond.
    """
    if bond.ndim == 1:
        return np.concatenate([bond[0:3], shift_site(bond[3:6])])
    else:
        return np.concatenate([bond[:, 0:3], shift_site(bond[:, 3:6])])


# ==================================================
def convert_to_fractional_hexagonal(vec_c):
    """
    Convert vector to fractional coordinate for hexagonal system.

    Args:
        vec_c (ndarray): vector in cartesian coordinate.

    Returns:
        - (ndarray) -- in fractional coordinate.
    """
    return convert_to_primitive("h", vec_c, shift=False)


# ==================================================
def convert_to_fractional_hexagonal_matrix(mat_c):
    """
    Convert matrix to fractional coordinate for hexagonal systems.

    Args:
        mat_c (ndarray): matrix in fractioanl coordinate.

    Returns:
        - (ndarray) -- in fractional coordinate.
    """
    return convert_to_primitive_matrix("h", mat_c)


# ==================================================
def convert_to_cartesian_hexagonal(vec_f):
    """
    Convert vector to cartesian coordinate for hexagonal system.

    Args:
        vec_f (ndarray): vector in fractional coordinate.

    Returns:
        - (ndarray) -- in cartesian coordinate.
    """
    return convert_to_conventional("h", vec_f, plus_set=False, shift=False)


# ==================================================
def convert_to_cartesian_hexagonal_matrix(mat_f):
    """
    Convert matrix to cartesian coordinate for hexagonal system.

    Args:
        mat_f (ndarray): matrix in fractioanl coordinate.

    Returns:
        - (ndarray) -- in cartesian coordinate.
    """
    return convert_to_conventional_matrix("h", mat_f)


# ==================================================
def convert_to_primitive(lattice, vec_cf, shift=True):
    """
    Convert vector to primitive cell in fractional coordinate.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        vec_cf (ndarray): vector of conventional cell in fractional coordinate.
        shift (bool, optional): shift to home cell ?

    Returns:
        - (ndarray) -- in primitive cell.
    """
    if lattice == "0":
        return vec_cf

    if lattice == "P":
        if shift:
            vec_cf = shift_site(vec_cf)
        return vec_cf
    else:
        if vec_cf.ndim == 1:
            vec_cf = np.pad(vec_cf, (0, 1), constant_values=1)
        else:
            vec_cf = np.pad(vec_cf, ((0, 0), (0, 1)), constant_values=1)

        Pi = Pi_dict[lattice]
        vec_pf = vec_cf @ Pi.T

        if shift:
            vec_pf = shift_site(vec_pf)

        if vec_pf.ndim == 1:
            vec_pf = vec_pf[0:3]
        else:
            vec_pf = vec_pf[:, 0:3]

        return vec_pf


# ==================================================
def convert_to_primitive_matrix(lattice, mat_cf):
    """
    Convert matrix to primitive cell in fractional coordinate.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        mat_cf (ndarray): matrix of conventional cell in fractional coordinate.

    Returns:
        - (ndarray) -- in primitive cell.
    """
    if lattice in ["P", "0"]:
        return mat_cf
    else:
        n = mat_cf.shape[-1]
        if n == 3:
            if mat_cf.ndim == 2:
                mat_cf = np.pad(mat_cf, ((0, 1), (0, 1)), constant_values=0)
                mat_cf[n, n] = 1
            else:
                mat_cf = np.pad(mat_cf, ((0, 0), (0, 1), (0, 1)), constant_values=0)
                mat_cf[:, n, n] = 1

        P = P_dict[lattice]
        Pi = Pi_dict[lattice]
        mat_pf = Pi @ mat_cf @ P

        if n == 3:
            if mat_pf.ndim == 2:
                mat_pf = mat_pf[0:3, 0:3]
            else:
                mat_pf = mat_pf[:, 0:3, 0:3]

        return mat_pf


# ==================================================
def convert_to_conventional(lattice, vec_pf, plus_set=False, shift=True):
    """
    Convert vector to conventional cell in fractional coordinate.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        vec_pf (ndarray): vector of primitive cell in fractional coordinate.
        plus_set (bool, optional): add partial translations ?
        shift (bool, optional): shift to home cell ?

    Returns:
        - (ndarray) -- in conventioanl cell.

    Note:
        - for plus_set, [set(t0), set(t1), ...].
    """
    if lattice == "0":
        return vec_pf

    if lattice == "P":
        if shift:
            vec_pf = shift_site(vec_pf)
        return vec_pf
    else:
        if vec_pf.ndim == 1:
            vec_pf = np.pad(vec_pf, (0, 1), constant_values=1)
        else:
            vec_pf = np.pad(vec_pf, ((0, 0), (0, 1)), constant_values=1)

        P = P_dict[lattice]
        vec_cf = vec_pf @ P.T

        if vec_cf.ndim == 1:
            vec_cf = vec_cf[0:3]
        else:
            vec_cf = vec_cf[:, 0:3]

        if plus_set:
            t = t_dict[lattice]
            vec_cf = np.concatenate([vec_cf + i for i in t])

        if shift:
            vec_cf = shift_site(vec_cf)

        return vec_cf


# ==================================================
def convert_to_conventional_matrix(lattice, mat_pf):
    """
    Convert matrix to conventional cell in fractional coordinate.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        mat_pf (ndarray): matrix of primitive cell in fractional coordinate.

    Returns:
        - (ndarray) -- in conventioanl cell.
    """
    if lattice in ["P", "0"]:
        return mat_pf
    else:
        n = mat_pf.shape[-1]
        if n == 3:
            if mat_pf.ndim == 2:
                mat_pf = np.pad(mat_pf, ((0, 1), (0, 1)), constant_values=0)
                mat_pf[n, n] = 1
            else:
                mat_pf = np.pad(mat_pf, ((0, 0), (0, 1), (0, 1)), constant_values=0)
                mat_pf[:, n, n] = 1

        P = P_dict[lattice]
        Pi = Pi_dict[lattice]
        mat_cf = P @ mat_pf @ Pi

        if n == 3:
            if mat_cf.ndim == 2:
                mat_cf = mat_cf[0:3, 0:3]
            else:
                mat_cf = mat_cf[:, 0:3, 0:3]

        return mat_cf
