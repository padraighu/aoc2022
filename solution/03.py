from typing import List

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("03")


def parse_input(input: str) -> List[str]:
    res = [l for l in input.splitlines() if len(l)]
    return res


def priority(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    if c.isupper():
        return ord(c) - 38
    return -1


def part_one(input: List[str]) -> int:
    res = 0
    for rucksack in input:
        idx = int(len(rucksack) / 2)
        first = rucksack[:idx]
        second = rucksack[idx:]
        overlap = set(first).intersection(set(second))
        assert len(overlap) == 1
        res += priority(overlap.pop())
    return res


def part_two(input: List[str]) -> int:
    res = 0
    for idx in range(0, len(input), 3):
        first = input[idx]
        second = input[idx + 1]
        third = input[idx + 2]
        overlap = set(first).intersection(set(second)).intersection(set(third))
        assert len(overlap) == 1
        res += priority(overlap.pop())
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 157), (REAL_INPUT, 7428)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 70), (REAL_INPUT, 2650)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
