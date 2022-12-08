from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

import pytest
from util import read_input

TEST_INPUT, REAL_INPUT = read_input("07")


class NodeType(Enum):
    File = 1
    Dir = 2


@dataclass
class FSNode:
    id: int
    name: str
    type: NodeType
    parent: int
    children: List[int]
    size: int = 0


def parse_input(input: str) -> List[FSNode]:
    lines = input.splitlines()
    child_lst: List[int] = []
    curr_node = FSNode(id=0, name="/", type=NodeType.Dir, children=[], parent=-1)
    res = [curr_node]
    id = 1
    child: Optional[FSNode]
    for l in lines[1:]:
        if l.startswith("$"):
            # finish adding the results of ls
            if child_lst:
                curr_node.children = child_lst
                child_lst = []
            cmd = l[2:4]
            if cmd == "cd":
                dest = l[5:]
                if dest == "..":
                    curr_node = res[curr_node.parent]
                else:
                    for child_id in curr_node.children:
                        if res[child_id].name == dest:
                            curr_node = res[child_id]
                            break
        else:
            # results of ls
            tokens = l.split(" ")
            if tokens[0] == "dir":
                child = FSNode(
                    id=id,
                    name=tokens[1],
                    type=NodeType.Dir,
                    children=[],
                    parent=curr_node.id,
                )
            else:
                child = FSNode(
                    id=id,
                    name=tokens[1],
                    type=NodeType.File,
                    size=int(tokens[0]),
                    children=[],
                    parent=curr_node.id,
                )
            res.append(child)
            id += 1
            child_lst.append(child.id)
    curr_node.children = child_lst

    def get_dir_size(dir_id: int) -> int:
        dir = res[dir_id]
        dir_size = 0
        for c in dir.children:
            if res[c].type is NodeType.File:
                dir_size += res[c].size
            elif res[c].type is NodeType.Dir:
                dir_size += get_dir_size(c)
        res[dir_id].size = dir_size
        return dir_size

    _ = get_dir_size(0)
    return res


def part_one(input: List[FSNode]) -> int:
    res = 0
    res = sum(
        [
            node.size
            for node in input
            if node.type is NodeType.Dir and node.size <= 100000
        ]
    )
    return res


def part_two(input: List[FSNode]) -> int:
    needed_space = input[0].size - 40000000
    res = min(
        [
            node.size
            for node in input
            if node.type is NodeType.Dir and node.size >= needed_space
        ]
    )
    return res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 95437), (REAL_INPUT, 1315285)])
def test_part_one(input: str, res: int) -> None:
    assert part_one(parse_input(input)) == res


@pytest.mark.parametrize("input, res", [(TEST_INPUT, 24933642), (REAL_INPUT, 9847279)])
def test_part_two(input: str, res: int) -> None:
    assert part_two(parse_input(input)) == res
