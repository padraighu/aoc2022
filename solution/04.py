from typing import List, Tuple

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("04")


def parse_input(input: str) -> List[Tuple[Tuple[int, int], ...]]:
    res = []
    for l in input.splitlines():
        curr = []
        for a in l.split(","):
            first, second = a.split("-")
            curr.append((int(first), int(second)))
        res.append(tuple(curr))
    return res


def part_one(input: List[Tuple[Tuple[int, int], ...]]) -> int:
    res = 0
    for first, second in input:
        if first[0] >= second[0] and first[1] <= second[1]:
            res += 1
        elif first[0] <= second[0] and first[1] >= second[1]:
            res += 1
    return res


def part_two(input: List[Tuple[Tuple[int, int], ...]]) -> int:
    res = 0
    for first, second in input:
        if first[1] >= second[0] and first[0] <= second[1]:
            res += 1
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 2), (REAL_INPUT, 490)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 4), (REAL_INPUT, 921)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
