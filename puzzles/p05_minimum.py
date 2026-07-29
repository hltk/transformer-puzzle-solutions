"""Puzzle 5 - minimum

Broadcast the minimum value of the sequence.
"""

from puzzles.base import indices, key, query, tokens


def minimum_spec(seq):
    m = min(seq)
    return [m for _ in seq]


def minimum(seq=tokens):
    smaller = (key(seq) < query(seq)).value(1)
    tiebreak = (
        (key(seq) == query(seq)) & (key(indices) < query(indices))
    ).value(1)
    return (
        (key(smaller) == query(0)) & (key(tiebreak) == query(0))
    ).value(seq)
