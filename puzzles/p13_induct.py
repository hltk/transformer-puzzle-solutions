"""Bonus 4 - induct

Induction-head style copy: at each position, copy the token that
followed the previous occurrence of the current token.
"""

from puzzles.base import indices, key, query, tokens, where


def induct_spec(default, seq):
    out = []
    for i in range(len(seq)):
        prev = None
        for j in range(i):
            if seq[j] == seq[i]:
                prev = j
        out.append(default if prev is None else seq[prev + 1])
    return out


def induct(default="_", seq=tokens):
    earlier = ((key(seq) == query(seq)) & (key(indices) < query(indices))).value(1)
    prev = ((key(seq) == query(seq)) & (query(earlier - 1) == key(earlier))).value(indices)
    followed = (query(prev + 1) == key(indices)).value(seq)
    return where(earlier == 0, default, followed)
