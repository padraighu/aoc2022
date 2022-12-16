from dataclasses import dataclass
from typing import Callable, List, Optional

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("11")


@dataclass
class Monkey:
    items: List[int]
    operation: Callable
    second_val: Optional[int]
    divisible_by: int
    dest_if_true: int
    dest_if_false: int


def parse_input(input: str) -> List[Monkey]:
    res = []
    for monkey_str in input.split("\n\n"):
        lines = monkey_str.split("\n")
        items = [int(i) for i in lines[1][lines[1].index(": ") + 1 :].split(", ")]
        operation_str = lines[2][lines[2].index("=") + 2 :]
        if operation_str[4] == "*":
            operation = int.__mul__
        else:
            operation = int.__add__
        if operation_str[6:].isnumeric():
            second_val = int(operation_str[6:])
        else:
            second_val = None
        divisible_by = int(lines[3].split("by ")[-1])
        dest_if_true = int(lines[4][-1])
        dest_if_false = int(lines[5][-1])
        monkey = Monkey(
            items, operation, second_val, divisible_by, dest_if_true, dest_if_false
        )
        res.append(monkey)
    return res


def _helper(monkeys: List[Monkey], part: int) -> int:
    assert part in (1, 2)
    res = 0
    rounds = 20 if part == 1 else 10000
    counter = [0 for _ in range(len(monkeys))]
    # this was the modular arithmetic trick for part 2 and I had to readup about it
    divisible_prod = 1
    for m in monkeys:
        divisible_prod *= m.divisible_by
    for _ in range(rounds):
        for idx, monkey in enumerate(monkeys):
            counter[idx] += len(monkey.items)
            while monkey.items:
                curr = monkey.items.pop(0)
                if monkey.second_val is None:
                    curr = monkey.operation(curr, curr)
                else:
                    curr = monkey.operation(curr, monkey.second_val)
                if part == 1:
                    curr = curr // 3
                else:
                    curr = curr % divisible_prod
                if not curr % monkey.divisible_by:
                    monkeys[monkey.dest_if_true].items.append(curr)
                else:
                    monkeys[monkey.dest_if_false].items.append(curr)
    counter = sorted(counter, reverse=True)
    res = counter[0] * counter[1]
    return res


def part_one(input: List[Monkey]) -> int:
    res = _helper(input, part=1)
    return res


def part_two(input: List[Monkey]) -> int:
    res = _helper(input, part=2)
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 10605), (REAL_INPUT, 56595)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize(
    "input, res", [(TEST_INPUT, 2713310158), (REAL_INPUT, 15693274740)]
)
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
