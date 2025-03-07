"""
For versatile.
"""

import time
import logging
import numpy as np
import sympy as sp
from sympy import SympifyError
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication, rationalize
from functools import wraps
from collections.abc import MutableMapping
from collections import namedtuple

from multipie2 import __top_dir__, TOL


# ==================================================
def apply_to_list(func, lst):
    """
    Apply function to each element of list.

    Args:
        func (function): function.
        lst (list): list.

    Returns:
        - (list) -- applied list.

    Note:
        - irregular-shaped list is acceptable.
    """
    if not isinstance(lst, list):
        return func(lst)

    result = []
    for sub_lst in lst:
        if isinstance(sub_lst, list):
            # apply function to sub list recursively.
            result.append(apply_to_list(func, sub_lst))
        else:
            # apply function to non list.
            result.append(func(sub_lst))
    return result


# ==================================================
def str_to_sympy(s, check_var=None, rational=True, subs=None):
    """
    Convert a string to a sympy.

    Args:
        s (str): a string.
        check_var (list, optional): variables to accept.
        rational (bool, optional): use rational number ?
        subs (dict, optional): replace dict for local variables.

    Returns:
        - (ndarray) -- (list of) sympy.

    Notes:
        - if format error occurs, raise ValueError.
        - if s cannot be converted to a sympy, raise ValueError.
    """
    if check_var is None:
        check_var = []

    check_var = set(check_var)

    transformations = standard_transformations + (implicit_multiplication,)
    if rational:
        transformations += (rationalize,)

    try:
        expression = parse_expr(s, transformations=transformations, local_dict=subs)
    except (SympifyError, SyntaxError, TypeError):
        raise ValueError(f"invalid string '{s}'.")
    var = set(get_variable(expression))
    if len(check_var) != 0 and not (var <= check_var):
        raise ValueError(f"invalid variable in '{s}'.")

    expression = np.asarray(expression)

    return expression


# ==================================================
def replace(a, s):
    """
    Replace expression (exchange among variables is ok).

    Args:
        a (ndarray): array.
        s (dict): dict for substitution.

    Returns:
        - (ndarray) -- replaced array.
    """
    return np.vectorize(lambda i: i.subs(s, simultaneous=True))(a)


# ==================================================
def get_variable(sp_ex, to_str=True):
    """
    Get variables used in a sympy expression.

    Args:
        sp_ex (sympy or ndarray): a sympy expression.
        to_str (bool, optional): convert to sorted str ?

    Returns:
        - (list) -- variable or sorted string.
    """
    sp_ex = np.asarray(sp_ex)
    sp_ex = sp.Matrix(sp_ex) if sp_ex.ndim > 0 else sp_ex.item()

    lst = list(sp_ex.free_symbols)
    if to_str:
        lst = sorted(map(str, lst))

    return lst


# ==================================================
def timer(func):
    """
    Timer decorater.

    Args:
        func (Function): function to decorate.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        logging.info(f"=== ({func.__name__}) begin === ")
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"=== ({func.__name__}) end ({end - start:.7f} [s] elapsed) ===")
        return result

    return wrapper


# ==================================================
def to_latex(a, style="scalar"):
    """
    convert list to latex list.

    Args:
        a (array-like): list of sympy.
        style (str, optional): style, "scalar/vector/matrix".

    Returns:
        - (list) -- list of LaTeX string without "$".
    """

    def vec_latex(m):
        s = r"\begin{pmatrix} "
        s += " & ".join([sp.latex(i) for i in m])
        s += r" \end{pmatrix}"
        return s

    def mat_latex(m):
        s = r"\begin{pmatrix} "
        s += r" \\ ".join([" & ".join([sp.latex(i) for i in row]) for row in m])
        s += r" \end{pmatrix}"
        return s

    if style == "scalar":
        return apply_to_list(sp.latex, a)
    elif style == "vector":
        if a.ndim == 1:
            return vec_latex(a)
        else:
            return [vec_latex(i) for i in a]
    elif style == "matrix":
        if a.ndim == 2:
            return mat_latex(a)
        else:
            return [mat_latex(i) for i in a]
    else:
        return ""


# ==================================================
def normalize_vector(vec, tol=TOL):
    """
    Normalize vector (sympy or complex/float).

    Args:
        vec (array-like): list of vectors.
        tol (float, optional): absolute norm tolerance for float.

    Returns:
        - (ndaray) -- normalized vector.
    """
    vec = np.asarray(vec)
    norm = np.linalg.norm if vec.dtype in [float, complex] else lambda x: sp.sqrt(np.dot(x.conjugate(), x))

    if vec.ndim == 1:
        n_vec = norm(vec)
        if n_vec > tol:
            vec /= n_vec
        return vec

    n_vec = np.apply_along_axis(norm, 1, vec)
    if vec.dtype in [float, complex]:
        n_vec[np.isclose(n_vec, tol)] = 1.0
    else:
        n_vec[n_vec == 0] = 1

    vec = vec / n_vec[:, np.newaxis]

    return vec


# ==================================================
def gram_schmidt(vec, n_max=None):
    """
    Gram-Schmidt orthogonalization (sympy).

    Args:
        vec (array-like): list of vectors to be orthogonalized, [[sympy]].
        n_max (int, optional): max. of nonzero basis.

    Returns:
        - (ndarray) -- list of nonzero orthogonalized vectors, [[sympy]].
        - (ndarray) -- indices of nonzero vectors, [int].
    """
    norm = lambda x: sp.sqrt(np.vdot(x, x))

    vec = np.asarray(vec, dtype=object)

    if vec.ndim < 2:
        nv = norm(vec)
        if nv != 0:
            vec /= nv
        return vec, np.array([0])

    if n_max is None:
        n_max = len(vec)

    ortho_vec = []
    nonzero = []
    for no, v in enumerate(vec):
        for u in ortho_vec:
            v -= np.vdot(v, u) / np.vdot(u, u) * u
        v = np.vectorize(sp.expand)(v)
        nv = norm(v)
        if nv != 0:
            ortho_vec.append(v / nv)
            nonzero.append(no)
        if len(ortho_vec) == n_max:
            break

    ortho_vec = np.asarray(ortho_vec)
    nonzero = np.asarray(nonzero)

    return ortho_vec, nonzero


# ==================================================
class Dict(MutableMapping):
    # ==================================================
    def __init__(self, name, field, *args, **kwargs):
        """
        Named tuple dict.

        Args:
            name (str): Dict name.
            field (list): field name.
        """
        self.key_type = namedtuple(name, field)
        self._data = dict(*args, **kwargs)

    # ==================================================
    def __getitem__(self, key):
        key = tuple(key) if isinstance(key, (list, tuple)) else (key,)  # for single value.
        return self._data[key]

    # ==================================================
    def __setitem__(self, key, value):
        key = tuple(key) if isinstance(key, (list, tuple)) else (key,)  # for single value.
        self._data[self.key_type(*key)] = value

    # ==================================================
    def __delitem__(self, key):
        key = tuple(key) if isinstance(key, (list, tuple)) else (key,)  # for single value.
        del self._data[key]

    # ==================================================
    def __iter__(self):
        return iter(self._data)

    # ==================================================
    def __len__(self):
        return len(self._data)

    # ==================================================
    def get(self, key, default=None):
        return self._data.get(key, default)

    # ==================================================
    def named_keys(self):
        """
        Keys as named tuple.

        Returns:
            - (dict_keys) -- named tuple keys.
        """
        return self._data.keys()

    # ==================================================
    def keys(self):
        if len(self.field) == 1:
            return dict.fromkeys(k[0] for k in self._data.keys()).keys()
        else:
            return dict.fromkeys(tuple(k) for k in self._data.keys()).keys()

    # ==================================================
    def values(self):
        return self._data.values()

    # ==================================================
    def named_items(self):
        """
        Items with named tuple keys.

        Returns:
            - (dict_items) -- items with named tuple keys.
        """
        return self._data.items()

    # ==================================================
    def items(self):
        return dict(zip(self.keys(), self.values())).items()

    # ==================================================
    @property
    def name(self):
        """
        Key field name.

        Returns:
            - (str) -- key field name.
        """
        return self.key_type.__name__

    # ==================================================
    @property
    def field(self):
        """
        Field names.

        Returns:
            - (list) -- field names.
        """
        return self.key_type._fields

    # ==================================================
    def select(self, **conditions):
        """
        Select dict by conditions.

        Returns:
            - (Dict) -- selected Dict.
        """
        result = {}
        for key, v in self._data.items():
            if all(getattr(key, attr) == value for attr, value in conditions.items()):
                result[key] = v
        return Dict(self.key_type.__name__, self.key_type._fields, result)

    # ==================================================
    def sort(self, *attributes):
        """
        Sort dict.

        Returns:
            - (Dict) -- sorted Dict.

        Note:
            - attributes: tuple for sort property.
                - ("key_name", custum order list, ascending?)
                - ("key_name", custum order list)
                - ("key_name", ascending?)
                - "key_name"
        """

        def sort_key(key):
            values = []
            for attr in attributes:
                if isinstance(attr, tuple):
                    if len(attr) == 3:
                        attr_name, order, asc = attr
                    elif len(attr) == 2:
                        if type(attr[1]) == list:
                            attr_name, order = attr
                            asc = True
                        else:
                            attr_name, asc = attr
                            order = None
                    else:
                        raise ValueError("Invalid attribute tuple format.")
                else:
                    attr_name, order, asc = attr, None, True

                value = getattr(key, attr_name)
                if order and isinstance(order, list):
                    # custum order.
                    idx = order.index(value) if value in order else float("inf")
                    values.append(idx if asc else -idx)
                else:
                    # sort by value.
                    values.append(value if asc else -value)
            return tuple(values)

        # sort.
        if len(attributes) == 0:
            attributes = self.key_type._fields
        sorted_keys = sorted(self._data.keys(), key=sort_key)
        return Dict(self.key_type.__name__, self.key_type._fields, {key: self[key] for key in sorted_keys})

    # ==================================================
    def __repr__(self):
        items = (f"{tuple(key)}: {value}" for key, value in self._data.items())
        return "{" + ", ".join(items) + "}"

    # ==================================================
    def __getstate__(self):
        return {
            "name": self.key_type.__name__,
            "field": self.key_type._fields,
            "data": {tuple(k): v for k, v in self._data.items()},
        }

    # ==================================================
    def __setstate__(self, state):
        self.key_type = namedtuple(state["name"], state["field"])
        self._data = {self.key_type(*k): v for k, v in state["data"].items()}


# ==================================================
def renumber(d, key):
    """
    Renumber Dict.

    Args:
        d (Dict): Dict.
        key (str): key for renumber.

    Returns:
        - (Dict) -- renumbered Dict.
    """
    dic = Dict(d.name, d.field)
    for idx, v in d.named_items():
        idx = idx._replace(**{key: -1})
        dic[idx] = dic.get(idx, []) + [v]

    rd = Dict(d.name, d.field)
    for idx, v in dic.named_items():
        if len(v) == 1:
            rd[idx] = v[0]
        else:
            for no, vi in enumerate(v):
                idx = idx._replace(**{key: no + 1})
                rd[idx] = vi

    return rd
