"""
For versatile (more).
"""

import os
import numpy as np
import sympy as sp
from fractions import Fraction

from multipie2 import __top_dir__, TOL
from multipie2.util.util import str_to_sympy, get_variable


# ==================================================
def write_data(filename, data, header=None, var=None, mode="w", verbose=False, subdir=None):
    """
    Write data into data folder.

    Args:
        filename (str): filename.
        data (Any): data to be written.
        header (str, optional): header string.
        var (str, optional): variable name.
        mode (str, optional): file mode.
        verbose (bool, optional): verbose info ?
        subdir (str, optional): sub directory.

    Notes:
        - data is written under "multipie2/data/".
    """
    if subdir is None:
        ofile = os.path.join(__top_dir__, "multipie2/data/", filename)
    else:
        ofile = os.path.join(__top_dir__, "multipie2/data/", subdir, filename)
    with open(ofile, mode=mode, encoding="utf-8") as f:
        if header is not None:
            print('"""' + header + '"""', file=f)
        s = "" if var is None else f"{var} ="
        print(s, data, file=f, end="\n\n")
        if verbose:
            print(f"save text to '{ofile}'.")


# ==================================================
def is_regular_list(lst):
    """
    Is regular-shaped list ?

    Args:
        lst (list): a list.

    Returns:
        - (bool) -- is regular-shaped list ?
    """
    try:
        np.array(lst)
        return True
    except ValueError:
        return False


# ==================================================
def str_to_numpy(s, digit=16, check_shape=None):
    """
    Convert a string (list) to a numpy array.

    Args:
        s (str): a string (list).
        digit (int, optional): accuracy digit.
        check_shape (tuple, optional): shape to check.

    Returns:
        - (ndarray) -- a numpy array.

    Note:
        - in check_shape, '0' means no check.
        - irregular-shaped list is not acceptable.
        - when error occurrs, raise ValueError.
    """
    sl = str_to_list(s)
    if not is_regular_list(sl):
        raise ValueError(f"invalid array in '{s}'.")

    tp = complex if s.count("I") > 0 or s.count("j") > 0 else float

    sl = np.array(sl)
    if check_shape is not None:
        if sl.ndim != len(check_shape):
            raise ValueError(f"invalid shape in '{s}'.")
        shape = sl.shape
        for i in range(len(shape)):
            if check_shape[i] > 0 and shape[i] != check_shape[i]:
                raise ValueError(f"invalid shape in '{s}'.")

    try:
        sl = np.vectorize(lambda x: str_to_sympy(x, rational=False))(sl)
        sl = np.vectorize(tp)(sl).round(digit)
    except:
        raise ValueError(f"invalid string '{s}'.")

    return sl


# ==================================================
def str_to_list(s):
    """
    Convert a string to a list of strings.

    Args:
        s (str): a string.

    Returns:
        - (list) -- a list of strings.

    Note:
        - irregular-shaped list is acceptable.
        - in case of a single value, return as it is.
        - raise ValueError for invalid string.
    """
    if s.count("[") != s.count("]"):
        raise ValueError(f"invalid string '{s}'.")

    if s.count("[") == 0:
        return s

    nested_list = []
    stack = []
    current_word = ""

    for char in s:
        if char == "[":
            if current_word.strip():  # remove space, and append it for non-null string.
                stack[-1].append(current_word.strip())
                current_word = ""
            stack.append([])
        elif char == "]":
            if current_word.strip():  # remove space, and append it for non-null string.
                stack[-1].append(current_word.strip())
                current_word = ""
            if stack:
                popped = stack.pop()
                if stack:
                    stack[-1].append(popped)
                else:
                    nested_list.append(popped)
        elif char == ",":
            if current_word.strip():  # remove space, and append it for non-null string.
                stack[-1].append(current_word.strip())
                current_word = ""
        else:
            current_word += char

    if current_word.strip():  # parse last word.
        if stack:
            stack[-1].append(current_word.strip())
        else:
            nested_list.append(current_word.strip())

    return nested_list[0]


# ==================================================
def to_fraction(x, max_denominator=1000000):
    """
    Convert float number to fractional one.

    Args:
        x (float): float number.
        max_denominator (int, optional): max. of denominator.

    Returns:
        - (str) -- fractional string.
    """
    return str(Fraction(x).limit_denominator(max_denominator))


# ==================================================
def convert_to_vector(v):
    """
    Convert xyz linear expression without const. to vector.

    Args:
        v (sympy or str): xyz linear expression.

    Returns:
        - (ndarray) -- vector expression, [sympy,sympy,sympy].
    """
    if type(v) == str:
        v = str_to_sympy(v).item()

    n, x, y, z = (
        np.array([sp.S(0), sp.S(0), sp.S(0)]),
        np.array([sp.S(1), sp.S(0), sp.S(0)]),
        np.array([sp.S(0), sp.S(1), sp.S(0)]),
        np.array([sp.S(0), sp.S(0), sp.S(1)]),
    )
    d = {str(i): v.coeff(i) for i in get_variable(v, False)}
    v = n if len(d) == 0 else d.get("x", sp.S(0)) * x + d.get("y", sp.S(0)) * y + d.get("z", sp.S(0)) * z

    return v


# ==================================================
def convert_to_spherical_coordinate(vec):
    """
    Convert to spherical coordinate from cartesian one.

    Args:
        vec (array-like): list of 3d vectors.

    Returns:
        - (ndarray) -- list of (r,theta,phi).
    """
    vec = np.asarray(vec)
    r = np.sqrt(vec[:, 0] ** 2 + vec[:, 1] ** 2 + vec[:, 2] ** 2)
    theta = np.arccos(vec[:, 2] / r)
    phi = np.mod(np.arctan2(vec[:, 1], vec[:, 0]), 2 * np.pi)
    sc = np.array(list(zip(r, theta, phi)))
    return sc


# ==================================================
def convert_to_cartesian_coordinate(vec_angle):
    """
    Convert to cartesian coordinate from spherical one.

    Args:
        vec_angle (array-like): list of (theta, phi).

    Returns:
        - (ndarray) -- list of 3d vectors (x,y,z).
    """
    vec_angle = np.asarray(vec_angle)
    pos = []
    for th, phi in vec_angle:
        x = np.sin(th) * np.cos(phi)
        y = np.sin(th) * np.sin(phi)
        z = np.cos(th)
        pos.append([x, y, z])
    pos = np.array(pos)

    return pos


# ==================================================
def sort_vector(vec):
    """
    Sort vector.

    Args:
        vec (array-like): list of vectors.

    Returns:
        - (ndarray) -- sorted vectors.
    """
    vec = np.asarray(vec)
    if vec.ndim == 1:
        return vec
    return np.asarray(sorted(vec.tolist(), key=lambda x: tuple(x)))


# ==================================================
def get_closest_vector(target, vec, tol=TOL):
    """
    Get closest vector.

    Args:
        target (array-like): vector.
        vec (array-like): list of vectors.
        tol (float, optional): absolute tolerance.

    Returns:
        - (int) -- index (when distance > tol, None).
    """
    target = np.asarray(target)
    vec = np.asarray(vec)

    distances = np.linalg.norm(vec - target, axis=1)
    idx = np.argmin(distances)
    if distances[idx] < tol:
        return idx
    else:
        return None


# ==================================================
def remove_duplicate_vector(vec, tol=TOL):
    """
    Remove duplicate vector.

    Args:
        vec (array-like): list of vectors.
        tol (float, optional): absolute tolerance.

    Returns:
        - (ndarray) -- vectors.
    """
    vec = np.asarray(vec)

    vecs = []
    for v in vec:
        if not any(np.allclose(v, uniq_vec, atol=tol) for uniq_vec in vecs):
            vecs.append(v)
    return np.array(vecs)
