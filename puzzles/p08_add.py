"""Puzzle 8 - add

Add two numbers written as a digit string with a single '+' separator.
"""

from puzzles.base import tokens, where
from puzzles.p02_shift import shift
from puzzles.p04_split import split
from puzzles.p07_slide import slide


def atoi(seq=tokens):
    return seq.map(lambda x: ord(x) - ord("0"))


def add_spec(seq):
    a, b = "".join(seq).split("+")
    c = int(a) + int(b)
    out = f"{c}"
    return list(map(int, list(("0" * (len(seq) - len(out))) + out)))


def add(seq=tokens):
    a = atoi(split("+", True, seq))
    b = atoi(split("+", False, seq))
    carry = where(a + b == 9, "<", where(a + b >= 10, "1", "0"))
    carry = shift(-1, "0", slide("<", carry))
    return (a + b + atoi(carry)) % 10
