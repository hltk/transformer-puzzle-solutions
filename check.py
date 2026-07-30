"""Minimal check: each solution matches its spec on a few examples."""

from puzzles.p00_head import head, head_spec
from puzzles.p01_index import index, index_spec
from puzzles.p02_shift import shift, shift_spec
from puzzles.p03_ralign import ralign, ralign_spec
from puzzles.p04_split import split, split_spec
from puzzles.p05_minimum import minimum, minimum_spec
from puzzles.p06_first import first, first_spec
from puzzles.p07_slide import slide, slide_spec
from puzzles.p08_add import add, add_spec
from puzzles.p09_reverse import reverse, reverse_spec
from puzzles.p10_histogram import histogram, histogram_spec

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
check("first", first(3)(SEQ), first_spec(3, SEQ))
check("first/str", first("l")(list("hello")), first_spec("l", list("hello")))
check("slide", slide("<")(list("1<<2")), slide_spec("<", list("1<<2")))
check("slide/2", slide("<")(list("3<<<1<<3")), slide_spec("<", list("3<<<1<<3")))
check("add", add()(list("22+384")), add_spec(list("22+384")))
check("add/carry", add()(list("99+1")), add_spec(list("99+1")))
check("add/long", add()(list("1+9999")), add_spec(list("1+9999")))
check("reverse", reverse()(SEQ), reverse_spec(SEQ))
check("reverse/str", reverse()(list("abcde")), reverse_spec(list("abcde")))
check("histogram", histogram()(SEQ), histogram_spec(SEQ))
check("histogram/str", histogram()(list("abacab")), histogram_spec(list("abacab")))
print("all ok")
