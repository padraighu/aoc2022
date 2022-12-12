from typing import List, Set, Tuple, Union

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("09")

DIRS = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}

Point = Union[List[int], Tuple[int, int]]


def parse_input(input: str) -> List[Tuple[Point, int]]:
    res: List[Tuple[Point, int]] = []
    for l in input.splitlines():
        l_split = l.split(" ")
        direction = DIRS[l_split[0]]
        step = int(l_split[1])
        res.append((direction, step))
    return res


def dist(x: Point, y: Point) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def _helper(input: List[Tuple[Point, int]], num_knots: int) -> int:
    knots = [[0, 0] for _ in range(num_knots)]
    visited: Set[Tuple[int, ...]] = set()
    for direction, step in input:
        for _ in range(step):
            for idx in range(num_knots - 1):
                head = knots[idx]
                tail = knots[idx + 1]
                if idx == 0:
                    head[0] += direction[0]
                    head[1] += direction[1]
                ht_dist = dist(head, tail)
                tail_should_move_one_direction = ht_dist == 2 and (
                    head[0] == tail[0] or head[1] == tail[1]
                )
                tail_should_move_diagonal = ht_dist > 2
                dy = head[0] - tail[0]
                dx = head[1] - tail[1]
                if tail_should_move_one_direction or tail_should_move_diagonal:
                    if dy:
                        tail[0] += 1 if dy > 0 else -1
                    if dx:
                        tail[1] += 1 if dx > 0 else -1
                    if idx == num_knots - 2:
                        visited.add(tuple(tail))
                knots[idx] = head
                knots[idx + 1] = tail
    res = len(visited) + 1
    return res


def part_one(input: List[Tuple[Point, int]]) -> int:
    res = _helper(input, num_knots=2)
    return res


def part_two(input: List[Tuple[Point, int]]) -> int:
    res = _helper(input, num_knots=10)
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 13), (REAL_INPUT, 5619)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 1), (REAL_INPUT, 2376)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
