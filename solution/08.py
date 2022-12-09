from typing import List, Tuple

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("08")

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_input(input: str) -> List[List[int]]:
    res = []
    for l in input.splitlines():
        col = [int(c) for c in l]
        res.append(col)
    return res


def is_visible(
    map: List[List[int]], tree: Tuple[int, int], delta: Tuple[int, int]
) -> bool:
    i, j = tree
    while 0 < i < len(map) - 1 and 0 < j < len(map[i]) - 1:
        i += delta[0]
        j += delta[1]
        if map[i][j] >= map[tree[0]][tree[1]]:
            return False
    return True


def part_one(input: List[List[int]]) -> int:
    nrow = len(input)
    ncol = len(input[0])
    res = 2 * (nrow + ncol) - 4
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if any([(is_visible(input, (i, j), d)) for d in DIRS]):
                res += 1
    return res


def viewing_distance(
    map: List[List[int]], tree: Tuple[int, int], delta: Tuple[int, int]
) -> int:
    i, j = tree
    res = 0
    while 0 < i < len(map) - 1 and 0 < j < len(map[i]) - 1:
        i += delta[0]
        j += delta[1]
        res += 1
        if map[i][j] >= map[tree[0]][tree[1]]:
            break
    return res


def part_two(input: List[List[int]]) -> int:
    nrow = len(input)
    ncol = len(input[0])
    res = -1
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            score = 1
            for dist in [viewing_distance(input, (i, j), d) for d in DIRS]:
                score *= dist
            res = max(score, res)
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 21), (REAL_INPUT, 1546)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 8), (REAL_INPUT, 1546)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
