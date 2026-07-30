"""Bonus 0 - reverse

Reverse the sequence end-to-end.
"""

from puzzles.base import indices, key, query, tokens


def reverse_spec(seq):
    return list(reversed(seq))


def reverse(seq=tokens):
    l = (key(1) == query(1)).value(1)
    return (key(indices) == query(l - indices - 1)).value(seq)
