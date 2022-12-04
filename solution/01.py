from typing import List

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("01")


def parse_input(input: str) -> List[List[int]]:
    res = []
    curr = []
    for l in input.splitlines():
        if len(l):
            curr.append(int(l))
        else:
            res.append(curr)
            curr = []
    res.append(curr)
    return res


def part_one(input: List[List[int]]) -> int:
    sums = [sum(e) for e in input]
    res = max(sums)
    return res


def part_two(input: List[List[int]]) -> int:
    sums = [sum(e) for e in input]
    res = sum(sorted(sums)[-3:])
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 24000), (REAL_INPUT, 70764)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 45000), (REAL_INPUT, 203905)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
