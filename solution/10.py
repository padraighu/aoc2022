from typing import List, Tuple

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("10")


Instruction = Tuple[str, int]


def parse_input(input: str) -> List[Instruction]:
    res = []
    for l in input.splitlines():
        if l == "noop":
            res.append(("noop", 0))
        else:
            res.append(("addx", int(l.split(" ")[1])))
    return res


def next_cycle_part_one(current_cycle: int, register: int, res: int) -> Tuple[int, int]:
    signal_strength = 0
    next = current_cycle + 1
    if next in range(20, 221, 40):
        signal_strength = register * next
        res += signal_strength
    return next, res


def part_one(input: List[Instruction]) -> int:
    instructions = input
    cycle = 0
    register = 1
    res = 0
    while instructions:
        curr_instruction, val = instructions.pop(0)
        cycle, res = next_cycle_part_one(cycle, register, res)
        if curr_instruction == "addx":
            cycle, res = next_cycle_part_one(cycle, register, res)
            register += val
    return res


def next_cycle_part_two(
    current_cycle: int, register: int
) -> Tuple[int, Tuple[int, int], str]:
    current_cycle += 1
    # translate cycle to the the current pixel being drawn
    j = (current_cycle % 40 - 1) % 40
    i = (current_cycle - 1) // 40
    # figure out what to draw at current pixel
    pixel = "."
    if register - 1 <= j <= register + 1:
        pixel = "#"
    return current_cycle, (i, j), pixel


def part_two(input: List[Instruction]) -> str:
    res = "\n"
    instructions = input
    cycle = 0
    register = 1
    crt = [["" for _c in range(40)] for _r in range(6)]
    while instructions:
        curr_instruction, val = instructions.pop(0)
        cycle, coord, pixel = next_cycle_part_two(cycle, register)
        crt[coord[0]][coord[1]] = pixel
        if curr_instruction == "addx":
            cycle, coord, pixel = next_cycle_part_two(cycle, register)
            crt[coord[0]][coord[1]] = pixel
            register += val
    for i in range(len(crt)):
        res += "".join(crt[i]) + "\n"
    print(res)
    return res


@pytest.mark.parametrize(
    "input, res",
    [
        (TEST_INPUT, 13140),
        (REAL_INPUT, 13860),
    ],
)
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


PART_TWO_TEST_EXPECTED = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

PART_TWO_REAL_EXPECTED = """
###..####.#..#.####..##....##..##..###..
#..#....#.#..#.#....#..#....#.#..#.#..#.
#..#...#..####.###..#.......#.#....###..
###...#...#..#.#....#.##....#.#....#..#.
#.#..#....#..#.#....#..#.#..#.#..#.#..#.
#..#.####.#..#.#.....###..##...##..###..
"""


@pytest.mark.parametrize(
    "input, res",
    [(TEST_INPUT, PART_TWO_TEST_EXPECTED), (REAL_INPUT, PART_TWO_REAL_EXPECTED)],
)
def test_part_two(input: str, res: str) -> None:
    assert part_two(parse_input(input)) == res
