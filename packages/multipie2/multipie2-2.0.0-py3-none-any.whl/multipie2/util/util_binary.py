"""
For binary data.
"""

import os
import gzip
import subprocess
import pickle
import copy
from multipie2 import __top_dir__


# ==================================================
class BinaryManager(dict):
    suffix = ".pkl"

    # ==================================================
    def __init__(self, filename=None, topdir=None, subdir=None, verbose=False, comment=""):
        """
        Binary data manager.

        Args:
            filename (str or list, optional): file name to load.
            topdir (str, optional): top directory. [default: multipie/binary_data]
            subdir (str, optional): sub directory.
            verbose (bool, optional): verbose comment ?
            comment (str, optional): comment.
        """
        self.topdir = topdir
        self.subdir = subdir
        self.verbose = verbose
        self.comment = ""
        self.add_comment(comment)

        if filename is not None:
            self.load(filename)

    # ==================================================
    def __str__(self):
        """
        Convert to str.

        Returns:
            - (str) -- comment of data.
        """
        return '"""\n' + self.comment.strip(" \n") + '\n"""'

    # ==================================================
    def __repr__(self):
        """
        Dump data.

        Returns:
            - (str) -- data string.
        """
        s = str(dict(super().items()))

        return s

    # ==================================================
    def set_topdir(self, topdir):
        """
        Set top directory.

        Args:
            topdir (str): top directory.
        """
        self.topdir = topdir

    # ==================================================
    def add_comment(self, comment):
        """
        Add comment.

        Args:
            comment (str): comment.
        """
        if comment != "":
            self.comment += comment.lstrip("\n").rstrip(" \n") + "\n"

    # ==================================================
    def set_subdir(self, subdir):
        """
        Set sub directory.

        Args:
            subdir (str): sub directory.
        """
        self.topdir = subdir

    # ==================================================
    def clear(self):
        """
        Clear data.
        """
        super().clear()
        self.comment = ""

    # ==================================================
    def to_dict(self):
        """
        Convert data to dict.

        Returns:
            - (dict) -- data in dict.
        """
        dic = {"header": self.comment, "data": dict(copy.deepcopy(self))}
        return dic

    # ==================================================
    def from_dict(self, d):
        """
        Set data from dict.
        """
        self.clear()
        self.update(d.get("data", {}))
        comment = d.get("header", "")
        if comment != "":
            self.add_comment(comment)

    # ==================================================
    def save(self, filename, detail=True):
        """
        Save data as binary.

        Args:
            filename (str): file name. (extension is .pkl).
            detail (bool, optional): detailed info. ?
        """
        fullpath = self.get_fullpath(filename)
        dic = self.to_dict()
        bs = pickle.dumps(dic, protocol=pickle.HIGHEST_PROTOCOL)
        with gzip.open(fullpath, mode="wb") as f:
            f.write(bs)

        if self.verbose:
            print(f"save binary to '{fullpath}'.")
            if detail:
                if self.comment != "":
                    print(self.__str__())
                info = list(self.keys())
                print(f"keys = {info}.")
                size = os.path.getsize(fullpath)
                print(f"binary size = {size:,} Bytes.")

    # ==================================================
    def load(self, filename):
        """
        Load binary data.

        Args:
            filename (str): file name. (extension is .pkl).
        """
        self.clear()
        fullpath = self.get_fullpath(filename)
        with gzip.open(fullpath, "rb") as f:
            bs = f.read()
        data = pickle.loads(bs)
        self.from_dict(data)

        if self.verbose:
            print(f"load binary from '{fullpath}'.")
            if self.comment != "":
                print(self.__str__())

    # ==================================================
    def get_cwd(self):
        """
        Get working directory.

        Returns:
            - (str) -- working directory.
        """
        if self.topdir is None:
            cwd = os.path.join(__top_dir__, "multipie2/binary_data/")
        else:
            cwd = self.topdir

        if self.subdir is not None:
            cwd = os.path.join(cwd, self.subdir)

        return cwd

    # ==================================================
    def get_fullpath(self, filename):
        """
        Get full path name.

        Args:
            filename (str): file name.

        Returns:
            - (str) -- full path name.
        """
        ext = os.path.splitext(filename)[1]
        if ext not in [self.suffix]:
            filename += self.suffix

        topdir = self.get_cwd()
        os.makedirs(topdir, exist_ok=True)
        ofile = os.path.join(topdir, filename)

        return ofile


# ==================================================
def convert_binary_to_text(filename):
    """
    Convert binary to text file.

    Args:
        filename (str or list): binary file name.

    Note:
        - when filename is list, use first one for text file name.
        - text file name becomes binary_filename_pkl.py.
    """
    bm = BinaryManager(filename, verbose=True)

    if type(filename) != str:
        filename = filename[0]

    if filename.endswith(BinaryManager.suffix):
        out_filename = filename.replace(BinaryManager.suffix, "_" + BinaryManager.suffix[1:] + ".py")
    else:
        out_filename = filename + "_" + BinaryManager.suffix[1:] + ".py"

    topdir = bm.get_cwd()
    out_filename = os.path.join(topdir, out_filename)

    with open(out_filename, mode="w", encoding="utf-8") as f:
        s = str(bm) + "\n" + f"{filename} =" + repr(bm)
        print(s, file=f)

    cmd = "black --line-length=300 *.py"
    subprocess.run(cmd, shell=True, capture_output=True, cwd=topdir, text=True)

    print(f"convert to '{out_filename}'.")
