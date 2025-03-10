# -*- coding: utf-8 -*-
# Copyright (c) 2023, KarjaKAK
# All rights reserved.

import os
from ast import literal_eval as leval
from dataclasses import dataclass, field
from itertools import islice
from pathlib import Path
from typing import Generator

from treeview import TreeView


@dataclass(frozen=True, slots=True)
class ParseData(TreeView):
    """Parsing Data in TreeView docs for TVG
    that helping update the fold selected function.
    """

    filename: str
    data: tuple[int] | None = field(kw_only=True)
    pos: int = 0
    size: int = 0

    def __post_init__(self):
        if not (filename := self.findext()):
            raise FileExistsError(f"This {self.filename!r} is not exist!")
        ParseData._validate(self.data)
        super(TreeView, self).__setattr__("filename", filename)

    @staticmethod
    def _validate(data: tuple[int]) -> None:
        """Validating the data types."""

        if not isinstance(data, tuple | None):
            raise TypeError("Need to be a tuple!")
        elif data and len(data) == 0:
            raise ValueError("Tuple cannot be empty!")
        elif data and not all(isinstance(i, int) for i in data):
            raise TypeError("Tuple need to have int types only!")
        return None

    def findext(self) -> str | None:
        """Checker file path existence with TreeView format file."""

        match Path(self.filename):
            case pt if pt.exists() and ".txt" in pt.name:
                return str(pt.absolute())[:-4]
            case pt if os.path.exists(f"{pt.absolute()}.txt"):
                return str(pt.absolute())
            case _:
                return None

    def check_exist(self) -> bool:
        """Cheking if parsed data file is exist."""

        return Path(f"{self.filename}.dat").exists()

    def _restStr(self, sentence: str) -> str:
        """To create identifier from a data."""

        return sentence.strip().replace(" ", "")[:81]

    def create_data(self) -> None:
        """Create parsed data."""

        storeDat = []
        if self.data:
            with open(f"{self.filename}.dat", "wb") as dwr:
                for n, d in self.getdata():
                    if n in self.data:
                        storeDat.append((n, self._restStr(d)))
                for dt in storeDat:
                    dwr.write(f"{dt}\n".encode())
        del storeDat

    def getkv(self) -> Generator | None:
        """Get existing keys and values"""

        if self.check_exist():
            with open(f"{self.filename}.dat", "rb") as dr:
                yield from (leval(i.decode().strip("\n")) for i in dr)

    def getkey(self) -> Generator | None:
        """Get existing keys"""

        if self.check_exist():
            with open(f"{self.filename}.dat", "rb") as dr:
                yield from (leval(i.decode().strip("\n"))[0] for i in dr)

    def parent_size(self) -> tuple[bool, int]:
        """Getting size from parent"""

        child = self.check_child(self.pos)
        if not child:
            size = 0
            for n, d in islice(self.getdata(), self.pos + 1, None):
                if d[0] == " ":
                    size += 1
                else:
                    break
            if size:
                return (True, size)
            else:
                return (False, size)
        else:
            return (False, 0)


    def update_data(self) -> tuple[int] | None:
        """To update parsed data with existing TVG doc."""

        if self.check_exist():
            try:
                update = []
                s = 0
                len_of_data = self.getdatanum() - 1
                parsize = self.parent_size()
                for k, v in self.getkv():
                    if k < self.pos:
                        update.append(k)
                    elif k == self.pos and (self.pos + self.size) == len_of_data:
                        update.append(k)
                    else:
                        k += self.size
                        if not all(parsize):
                            for n, d in islice(self.getdata(), s, None):
                                if k == n:
                                    if self._restStr(d) == v:
                                        update.append(n)
                                        s = n + 1
                                        break
                            else:
                                s = k
                        else:
                            chk = self.pos + parsize[1]
                            for n, d in islice(self.getdata(), s, None):
                                if k == n:
                                    if self._restStr(d) == v:
                                        update.append(n)
                                        s = n + 1
                                        break
                                elif k - self.size == n and n <= chk:
                                    if self._restStr(d) == v:
                                        update.append(n)
                                        s = n + 1
                                        break

                            else:
                                s = k
                            del chk
                match update := tuple(update):
                    case update if update != tuple(self.getkey()):
                        super(ParseData, self).__setattr__("data", update)
                        self.create_data()
                        return self.data
                    case _:
                        return
            finally:
                del update, s, len_of_data, parsize

    def update_single_data(self, row: int) -> tuple[int] | None:
        """Update a single data to preserve"""

        if self.check_exist():
            try:
                match dt := tuple(self.getkey()):
                    case dt if row in dt:
                        super(ParseData, self).__setattr__("data", dt)
                        self.create_data()
                        return self.data
                    case _:
                        return
            finally:
                del dt, row

    def update_move(self, row: int, down: bool = False) -> tuple[int] | None:
        """Updating Data in moving a row up or down"""

        try:
            update = []
            s = 0
            getdatnum = self.getdatanum()
            for k in self.getkey():
                if k < row:
                    if down:
                        if self.check_child(k):
                            update.append(k)
                    else:
                        update.append(k)
                else:
                    if k == row:
                        if down:
                            update.append(k - 1)
                        else:
                            update.append(k + 1)
                    else:
                        update.append(k)

            match update := tuple(update):
                case update if update != tuple(self.getkey()):
                    super(ParseData, self).__setattr__("data", update)
                    self.create_data()
                    return self.data
                case _:
                    return
        finally:
            del update, s

    def check_child(self, row: int) -> bool:
        """Checking for specific row as a child in data"""

        for _, p in islice(self.getdata(), row, row + 1):
            if p[0] == "\n":
                return False
            elif p[0] == " ":
                return True
            else:
                return False

    def add_stacks(self) -> Generator | None:
        """Collect '+' sequence from start to end"""

        if self.check_exist():
            try:
                sequence = []
                pos = None
                for n, s in self.getdata():
                    if s[0] == "+":
                        pos = n
                    elif s == "\n":
                        if pos or pos == 0:
                            sequence.append(n - 1)
                            pos = None
                    elif n == self.getdatanum() - 1:
                        if pos or pos == 0:
                            sequence.append(n)
                if sequence:
                    return (i for i in sequence)
            finally:
                del sequence, pos

    def update_data_sum(self, plus: bool = True) -> tuple | None:
        """Update stacks for  SumAll data in TVG"""

        if self.check_exist():
            try:
                num = 0
                dat = []
                stack = []
                for i in self.add_stacks():
                    for k in self.getkey():
                        k = k + num if plus else k - num
                        if not stack:
                            if k <= i:
                                if k not in dat:
                                    dat.append(k)
                            else:
                                stack.append(i)
                                num += 1
                                break
                        elif k > stack[-1]:
                            if k <= i:
                                if k not in dat:
                                    dat.append(k)
                            else:
                                stack.append(i)
                                num += 1
                                break
                if dat := tuple(dat):
                    super(ParseData, self).__setattr__("data", dat)
                    self.create_data()
                    return self.data
            finally:
                del num, dat, stack

    def del_data(self) -> None:
        """Delete parsed data."""

        pth = f"{self.filename}.dat"
        if self.check_exist():
            os.remove(f"{pth}")
        del pth
