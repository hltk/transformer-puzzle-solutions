"""Minimal check: each solution matches its spec on a few examples."""

from puzzles.p00_head import head, head_spec
from puzzles.p01_index import index, index_spec
from puzzles.p02_shift import shift, shift_spec
from puzzles.p03_ralign import ralign, ralign_spec
from puzzles.p04_split import split, split_spec
from puzzles.p05_minimum import minimum, minimum_spec

SEQ = [2, 1, 3, 2, 4]
SEQ2 = [3, 4, 3, -1, 2]


def check(name, got, want):
    got = got.toseq() if hasattr(got, "toseq") else list(got)
    assert got == want, f"{name}: {got} != {want}"
    print(name, "ok")


check("head", head()(SEQ), head_spec(SEQ))
check("index", index(2)(SEQ), index_spec(2, SEQ))
check("shift", shift(2, 0)(SEQ), shift_spec(2, 0, SEQ))
check(
    "ralign",
    ralign("0")(list("xyz___")),
    ralign_spec("0", list("xyz___")),
)
check(
    "ralign/mid",
    ralign("0")(list("x_yz__")),
    ralign_spec("0", list("x_yz__")),
)
check(
    "split/1",
    split("-", 1)(list("xyz-ax")),
    split_spec("-", 1, list("xyz-ax")),
)
check(
    "split/0",
    split("-", 0)(list("xyz-ax")),
    split_spec("-", 0, list("xyz-ax")),
)
check("minimum", minimum()(SEQ), minimum_spec(SEQ))
check("minimum/tie", minimum()([2, 1, 1]), minimum_spec([2, 1, 1]))
print("all ok")
