"""Puzzle 6 - first

Broadcast the first index where the sequence equals token.
"""

from puzzles.base import indices, key, query, tokens


def first_spec(token, seq):
    first = None
    for i, s in enumerate(seq):
        if s == token and first is None:
            first = i
    return [first for _ in seq]


def first(token, seq=tokens):
    tiebreak = (
        (key(seq) == query(token)) & (key(indices) < query(indices))
    ).value(1)
    return (
        (key(seq) == query(token)) & (key(tiebreak) == query(0))
    ).value(indices)
