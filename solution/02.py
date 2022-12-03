from enum import Enum
from typing import List, Tuple

import pytest
from util import read_input


class Shape(Enum):
    Rock = "Rock"
    Paper = "Paper"
    Scissors = "Scissors"


STRING_TO_SHAPE_PT_1 = {
    "A": Shape.Rock,
    "B": Shape.Paper,
    "C": Shape.Scissors,
    "X": Shape.Rock,
    "Y": Shape.Paper,
    "Z": Shape.Scissors,
}

STRING_TO_SHAPE_PT_2 = {
    "A": Shape.Rock,
    "B": Shape.Paper,
    "C": Shape.Scissors,
}

STRING_TO_OUTCOME_PT_2 = {"X": 0, "Y": 3, "Z": 6}

SHAPE_SCORE = {Shape.Rock: 1, Shape.Paper: 2, Shape.Scissors: 3}

GAME_SCORE = {
    (Shape.Paper, Shape.Rock): 0,
    (Shape.Scissors, Shape.Paper): 0,
    (Shape.Rock, Shape.Scissors): 0,
    (Shape.Rock, Shape.Rock): 3,
    (Shape.Paper, Shape.Paper): 3,
    (Shape.Scissors, Shape.Scissors): 3,
    (Shape.Scissors, Shape.Rock): 6,
    (Shape.Rock, Shape.Paper): 6,
    (Shape.Paper, Shape.Scissors): 6,
}

MY_STRATEGY_PT_2 = {
    (Shape.Rock, 0): Shape.Scissors,
    (Shape.Paper, 0): Shape.Rock,
    (Shape.Scissors, 0): Shape.Paper,
    (Shape.Rock, 3): Shape.Rock,
    (Shape.Paper, 3): Shape.Paper,
    (Shape.Scissors, 3): Shape.Scissors,
    (Shape.Rock, 6): Shape.Paper,
    (Shape.Paper, 6): Shape.Scissors,
    (Shape.Scissors, 6): Shape.Rock,
}

TEST_INPUT, REAL_INPUT = read_input("02")


def parse_input_pt_1(input: str) -> List[Tuple[Shape, Shape]]:
    res = []
    for l in input.splitlines():
        opp_str, player_str = l.split(" ")
        opp = STRING_TO_SHAPE_PT_1[opp_str]
        player = STRING_TO_SHAPE_PT_1[player_str]
        res.append((opp, player))
    return res


def parse_input_pt_2(input: str) -> List[Tuple[Shape, int]]:
    res = []
    for l in input.splitlines():
        opp_str, outcome_str = l.split(" ")
        opp = STRING_TO_SHAPE_PT_1[opp_str]
        outcome = STRING_TO_OUTCOME_PT_2[outcome_str]
        res.append((opp, outcome))
    return res


def part_one(input: List[Tuple[Shape, Shape]]) -> int:
    res = 0
    for game in input:
        opp, player = game
        res += SHAPE_SCORE[player]
        res += GAME_SCORE[game]
    return res


def part_two(input: List[Tuple[Shape, int]]) -> int:
    res = 0
    for game in input:
        opp, outcome = game
        player = MY_STRATEGY_PT_2[game]
        res += SHAPE_SCORE[player]
        res += outcome
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 15), (REAL_INPUT, 11475)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input_pt_1(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 12), (REAL_INPUT, 16862)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input_pt_2(input)) == res
