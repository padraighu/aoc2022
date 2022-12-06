import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("06")


def parse_input(input: str) -> str:
    return input


def _helper(input: str, distinct_count: int) -> int:
    res = -1
    for idx in range(len(input) - distinct_count):
        slice = input[idx : idx + distinct_count]
        if len(set(slice)) == distinct_count:
            res = idx + distinct_count
            break
    return res


def part_one(input: str) -> int:
    res = _helper(input, 4)
    return res


def part_two(input: str) -> int:
    res = _helper(input, 14)
    return res


@pytest.mark.parametrize(
    "input, res",
    [
        (TEST_INPUT, 7),
        (REAL_INPUT, 1262),
    ],
)
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize(
    "input, res",
    [
        (TEST_INPUT, 19),
        (REAL_INPUT, 3444),
    ],
)
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
