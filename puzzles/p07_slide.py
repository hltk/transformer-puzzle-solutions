"""Puzzle 7 - slide

Replace each '<' with the closest non-'<' value to its right.
"""

from puzzles.base import indices, key, query, tokens


def slide_spec(match, seq):
    out = []
    for i, s in enumerate(seq):
        if s == match:
            for v in seq[i + 1 :]:
                if v != match:
                    out.append(v)
                    break
        else:
            out.append(s)
    return out


def slide(match="<", seq=tokens):
    count = ((key(seq) != query(match)) & (key(indices) >= query(indices))).value(1)
    return ((key(seq) != query(match)) & (key(count) == query(count))).value(seq)
