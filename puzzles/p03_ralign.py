"""Puzzle 3 - ralign

Right-align a sequence padded on the right with underscores.
"""

from puzzles.base import indices, key, query, tokens
from puzzles.p02_shift import shift


def ralign_spec(ldefault="0", seq=None):
    last = None
    for i in range(len(seq) - 1, -1, -1):
        if seq[i] == "_":
            last = i
        else:
            break
    if last is None:
        return seq
    return [ldefault] * (len(seq) - last) + seq[:last]


def ralign(ldefault="0", seq=tokens):
    has_non_pad_after = ((query("_") != key(seq)) & (key(indices) > query(indices))).value(1)
    cut = ((key(has_non_pad_after) == query(0)) & (query("_") == key(seq))).value(1)
    return shift(cut, ldefault, seq)
