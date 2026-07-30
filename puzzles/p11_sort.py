"""Bonus 2 - sort

Return the sequence values in ascending order.
"""

from puzzles.base import indices, key, query, tokens


def sort_spec(seq):
    return sorted(seq)


def sort(seq=tokens):
    mi = (key(seq) < query(seq)).value(1)
    tieb = ((key(seq) == query(seq)) & (key(indices) < query(indices))).value(1)
    return (key(mi + tieb) == query(indices)).value(seq)
