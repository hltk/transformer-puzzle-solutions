"""Puzzle 1 - index

Broadcast the element at a given index across the sequence.
"""

from puzzles.base import indices, key, query, tokens


def index_spec(i, seq):
    return [seq[i] for _ in seq]


def index(i, seq=tokens):
    return (key(indices) == query(i)).value(seq)
