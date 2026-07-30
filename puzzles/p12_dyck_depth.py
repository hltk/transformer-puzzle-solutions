"""Bonus 3 - dyck_depth

Nesting depth after each parenthesis in a Dyck-1 string.
"""

from puzzles.base import indices, key, query, tokens


def dyck_depth_spec(seq):
    depth = 0
    out = []
    for c in seq:
        if c == "(":
            depth += 1
            out.append(depth)
        elif c == ")":
            out.append(depth)
            depth -= 1
        else:
            raise ValueError(f"expected paren, got {c!r}")
    return out


def dyck_depth(seq=tokens):
    a = ((key(seq) == query("(")) & (query(indices) >= key(indices))).value(1)
    b = ((key(seq) == query(")")) & (query(indices) > key(indices))).value(1)
    return a - b
