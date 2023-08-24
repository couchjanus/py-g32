# test_set_done_task.py
import json
import pytest

from todo import (
    SUCCESS,
    ID_ERROR,
    controller,
)


test_todo1 = {
    "Task": "Get some milk.",
    "Priority": 2,
    "Done": True,
}
test_todo2 = {}


@pytest.mark.parametrize(
    "todo_id, expected",
    [
        pytest.param(1, (test_todo1, SUCCESS)),
        pytest.param(3, (test_todo2, ID_ERROR)),
    ],
)

def test_set_done(mock_json_file, todo_id, expected):
    todos = controller.Todo(mock_json_file)
    assert todos.set_done(todo_id) == expected
