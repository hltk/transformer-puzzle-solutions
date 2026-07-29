"""Puzzle 4 - split

Split on a separator value and keep the first or second part, right-aligned.
"""

from puzzles.base import indices, key, query, tokens, where
from puzzles.p03_ralign import ralign, ralign_spec


def split_spec(v, get_first_part, seq):
    out = []
    mid = False
    blank = "0" if not get_first_part else "_"
    for j, s in enumerate(seq):
        if s == v:
            out.append(blank)
            mid = True
        elif (get_first_part and not mid) or (not get_first_part and mid):
            out.append(s)
        else:
            out.append(blank)
    return ralign_spec("0", seq=out)


def split(v, get_first_part, seq=tokens):
    i = (query(v) == key(seq)).value(indices)
    blank = "0" if not get_first_part else "_"
    x = where((i > indices) if get_first_part else (i < indices), seq, blank)
    return ralign("0", x)
