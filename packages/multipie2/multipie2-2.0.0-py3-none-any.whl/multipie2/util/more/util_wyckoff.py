"""
For Wyckoff position.
"""

import numpy as np

from multipie2.data.data_crystal import t_dict
from multipie2 import TOL, DIGIT
from multipie2.util.util import str_to_sympy
from multipie2.util.more.util_more import remove_duplicate_vector, get_closest_vector


SHIFT = 1.0 - TOL
TOL_SAME_SITE = 1e-8

t_dict = {lattice: None if t is None else str_to_sympy(t).astype(float) for lattice, t in t_dict.items()}


# ==================================================
def equivalent_site(lattice, site_cf, so_cf):
    """
    Equivalent site.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        site_cf (array-like): site in conventional cell in fractional coordinate.
        so_cf (array-like): symmetry operation matrices in conventional cell in fractional coordinate.

    Returns:
        - (ndarray) -- equivalent sites including plus set in conventional cell in fractional coordinate.

    Note:
        - for space group, site is shifted within home unit cell, and with plus set.
    """
    so_cf = np.asarray(so_cf)
    site_cf = np.asarray(site_cf)

    if lattice == "0":
        site_list_cf = (so_cf @ site_cf).round(DIGIT)
        site_list_cf = remove_duplicate_vector(site_list_cf, TOL_SAME_SITE)
        return site_list_cf

    site_cf = np.pad(site_cf, (0, 1), constant_values=1.0)
    site_list_cf = so_cf @ site_cf
    site_list_cf = site_list_cf[:, 0:3]

    t = t_dict[lattice]
    site_list_cf = np.concatenate([site_list_cf + i for i in t]).round(DIGIT)
    site_list_cf = np.mod(site_list_cf, SHIFT)
    site_list_cf = remove_duplicate_vector(site_list_cf, TOL_SAME_SITE)

    return site_list_cf


# ==================================================
def evaluate_wyckoff(lattice, wyckoff_cf, site):
    """
    Evaluate Wyckoff position.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        wyckoff_cf (ndarray): Wyckoff position list, (conventional, fractional).
        site (dict): site dict, { "x": x, "y": y, "z": z }.

    Returns:
        - (ndarray) -- Wyckoff position sites (conventional, fractional, with plus set).
    """
    sx, sy, sz = site["x"], site["y"], site["z"]
    pos_cf = np.vectorize(lambda i: i.subs({"x": sx, "y": sy, "z": sz}))(wyckoff_cf).astype(float)

    if lattice != "0":
        t = t_dict[lattice]
        pos_cf = np.mod(np.concatenate([pos_cf + p for p in t]), SHIFT)
    pos_cf = pos_cf.round(DIGIT)

    return pos_cf


# ==================================================
def parse_wyckoff(pos):
    """
    Parse Wyckoff position.

    Args:
        pos (array-like): Wyckoff position of (x,y,z).

    Returns:
        - (ndarray) -- coefficient matrix, A.
        - (ndarray) -- constant vector, b.

    Note:
        - [f1(x,y,z),f2(x,y,z),f3(x,y,z)]^t = A [x,y,z]^t + b.
    """
    const = [p.subs({"x": 0.0, "y": 0.0, "z": 0.0}) for p in pos]
    pos = [p - c for p, c in zip(pos, const)]
    xc = [float(p.subs({"x": 1.0, "y": 0.0, "z": 0.0})) for p in pos]
    yc = [float(p.subs({"x": 0.0, "y": 1.0, "z": 0.0})) for p in pos]
    zc = [float(p.subs({"x": 0.0, "y": 0.0, "z": 1.0})) for p in pos]
    const = [float(i) for i in const]
    A = np.array([xc, yc, zc]).T
    b = np.asarray(const).T

    return A, b


# ==================================================
def find_wyckoff_xyz(pos, site):
    """
    Find (x,y,z) in Wyckoff position.

    Args:
        pos (array-like): Wyckoff position.
        site (array-like): site to match.

    Returns:
        - (dict) -- solution.
        - (float) -- residual difference.
    """
    s = np.asanyarray(site).T
    A, b = parse_wyckoff(pos)
    for ai, ci in zip(A, s - b):
        if np.linalg.norm(ai) < TOL_SAME_SITE and ci > TOL_SAME_SITE:
            return None, 100 * TOL_SAME_SITE
    solution, residual = np.linalg.lstsq(A, s - b, rcond=None)[:2]
    if len(residual) == 0:
        diff = 0.0
    else:
        diff = residual[0]
    solution = dict(zip(["x", "y", "z"], solution))
    return solution, diff


# ==================================================
def check_wyckoff(lattice, wyckoff_cf, solution, site):
    """
    Check if site belongs to Wyckoff position.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        wyckoff_cf (str): Wyckoff position list, (conventional, fractional).
        solution (dict): solution.
        site (array-like): site.

    Returns:
        - (bool) -- site within Wyckoff position sites ?
    """
    site = np.asarray(site)

    pos = evaluate_wyckoff(lattice, wyckoff_cf, solution)
    if lattice != "0":
        site = np.mod(site, SHIFT)
    idx = get_closest_vector(site, pos, TOL_SAME_SITE)

    return idx is not None


# ==================================================
def _find_wyckoff_position(site_cf, lattice, so_cf, wyckoff_cf):
    """
    Find Wyckoff position.

    Args:
        site_cf (array-like): site to find Wyckoff position.
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        so_cf (array-like): symmetry operations in conventional cell in fractional coordinate.
        wyckoff_cf (dict): Wyckoff dict for given group.

    Returns:
        - (str) -- Wyckoff position.
        - (ndarray) -- first Wyckoff position site.
    """
    so_cf = np.asarray(so_cf, dtype=float)
    site_cf = np.asarray(site_cf, dtype=float)
    if lattice != "0":
        site_cf = np.mod(site_cf, SHIFT)

    # equivalent sites.
    sites = equivalent_site(lattice, site_cf, so_cf)
    n = len(sites)

    # candidate Wyckoff positions.
    wp_list = [wp for wp in wyckoff_cf.keys() if int(wp[:-1]) == n]

    # list of Wyckoff position sites.
    if lattice == "0":
        wp_pos_list = [wyckoff_cf[wp]["expression"] for wp in wp_list]
    else:
        t = t_dict[lattice]
        wp_pos_list = [np.concatenate([wyckoff_cf[wp]["expression"] + p for p in t]).tolist() for wp in wp_list]

    # find Wyckoff position to match with given site.
    if lattice == "0":
        shift = np.array([[0, 0, 0]])
    else:
        shift = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    s0 = sites[0]
    for wp, pos_list in zip(wp_list, wp_pos_list):
        pos_list = np.concatenate([pos_list + s for s in shift])
        for pos in pos_list:
            sol, diff = find_wyckoff_xyz(pos, s0)
            if diff < TOL and check_wyckoff(lattice, wyckoff_cf[wp]["expression"], sol, site_cf):
                return wp, np.asarray([p.subs(sol) for p in pos_list[0]], dtype=float)

    return "-", np.asarray([0.0, 0.0, 0.0])


# ==================================================
def find_wyckoff_position(g, site):
    """
    Find Wyckoff position.

    Args:
        g (BinaryManager): group dict.
        site (array-like): site to find Wyckoff position (fractional, conventional).

    Returns:
        - (str) -- Wyckoff position.
        - (ndarray) -- first Wyckoff position site.
    """
    if type(site) == str:
        site = str_to_sympy(site)
    lattice = g["info"]["lattice"]
    so_cf = g["symmetry_operation"]["fractional"]
    wyckoff_cf = g["wyckoff"]["site"]

    wp, p0 = _find_wyckoff_position(site, lattice, so_cf, wyckoff_cf)
    return wp, p0
