# test_remove_task

import json
import pytest

from todo import (
    SUCCESS,
    ID_ERROR,
    controller,
)


test_todo3 = {
    "Task": "Get some milk.",
    "Priority": 2,
    "Done": False,
}
test_todo4 = {}


@pytest.mark.parametrize(
    "todo_id, expected",
    [
        pytest.param(1, (test_todo3, SUCCESS)),
        pytest.param(3, (test_todo4, ID_ERROR)),
    ],
)
def test_remove(mock_json_file, todo_id, expected):
    todos = controller.Todo(mock_json_file)
    assert todos.remove(todo_id) == expected


def test_remove_all(mock_json_file):
    todos = controller.Todo(mock_json_file)
    assert todos.remove_all() == ({}, SUCCESS)
