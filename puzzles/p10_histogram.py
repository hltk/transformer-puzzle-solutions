"""Bonus 1 - histogram

For each position, count how often its value appears in the sequence.
"""

from puzzles.base import key, query, tokens


def histogram_spec(seq):
    return [seq.count(x) for x in seq]


def histogram(seq=tokens):
    return (key(seq) == query(seq)).value(1)
