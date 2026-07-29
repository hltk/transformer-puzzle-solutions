"""Puzzle 2 - shift

Shift the sequence right by i, filling on the left with default.
"""

from puzzles.base import indices, key, query, tokens


def shift_spec(i, default="0", seq=None):
    return [default] * i + [s for j, s in enumerate(seq) if j < len(seq) - i]


def shift(i, default="0", seq=tokens):
    return (key(indices) == query(indices - i)).value(seq, default=default)
