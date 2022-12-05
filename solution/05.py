from collections import deque
from dataclasses import dataclass
from typing import Deque, List, Tuple

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("05")

Stack = Deque[str]


@dataclass
class Procedure:
    qty: int
    src: int
    dest: int


def parse_input(input: str) -> Tuple[List[Stack], List[Procedure]]:
    procedures = []
    lines = input.splitlines()
    sep_idx = lines.index("")
    stack_lines = lines[:sep_idx]
    procedure_lines = lines[sep_idx + 1 :]
    stack_nums = [int(stack_num.strip()) for stack_num in stack_lines[-1].split("   ")]
    stack_count = max(stack_nums)
    stacks = [deque([]) for _ in range(stack_count)]  # type: List[Stack]
    for l in stack_lines[:-1]:
        crate_begin_indices = [idx for idx, c in enumerate(l) if c == "["]
        for idx in crate_begin_indices:
            assert idx % 4 == 0
            curr_stack = idx // 4
            stacks[curr_stack].append(l[idx + 1])

    for l in procedure_lines:
        tokens = l.split(" ")
        procedure = Procedure(
            qty=int(tokens[1]), src=int(tokens[3]), dest=int(tokens[5])
        )
        procedures.append(procedure)
    res = (stacks, procedures)
    return res


def _helper(stacks: List[Stack], procedures: List[Procedure], part: int) -> str:
    assert part in (1, 2)
    for procedure in procedures:
        to_move = []
        for _ in range(procedure.qty):
            to_move.append(stacks[procedure.src - 1].popleft())
        while to_move:
            curr = to_move.pop(0) if part == 1 else to_move.pop()
            stacks[procedure.dest - 1].appendleft(curr)
    res = "".join([s.popleft() for s in stacks])
    return res


def part_one(input: Tuple[List[Stack], List[Procedure]]) -> str:
    return _helper(stacks=input[0], procedures=input[1], part=1)


def part_two(input: Tuple[List[Stack], List[Procedure]]) -> str:
    return _helper(stacks=input[0], procedures=input[1], part=2)


@pytest.mark.parametrize(
    "input, res",
    [
        (TEST_INPUT, "CMZ"),
        (REAL_INPUT, "VWLCWGSDQ"),
    ],
)
def test_part_one(input: str, res: str) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize(
    "input, res",
    [
        (TEST_INPUT, "MCD"),
        (REAL_INPUT, "TCGLQSLPW"),
    ],
)
def test_part_two(input: str, res: str) -> None:
    assert part_two(parse_input(input)) == res
