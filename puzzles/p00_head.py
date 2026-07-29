"""Puzzle 0 - head

Broadcast the first element across the sequence.
"""

from puzzles.base import indices, key, query, tokens


def head_spec(seq):
    return [seq[0] for _ in seq]


def head(seq=tokens):
    return (key(indices) == query(0)).value(seq)
