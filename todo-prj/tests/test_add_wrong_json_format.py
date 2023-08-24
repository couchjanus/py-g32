# test_add_wrong_json_format.py

import json
import pytest

from todo import (
    SUCCESS,
    controller,
)

test_data1 = {
    "task": ["Clean", "the", "house"],
    "priority": 1,
    "todo": {
        "Task": "Clean the house.",
        "Priority": 1,
        "Done": False,
    },
}

@pytest.fixture
def mock_wrong_json_format(tmp_path):
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        db.write("")
    return db_file


def test_add_wrong_json_format(mock_wrong_json_format):
    todos = controller.Todo(mock_wrong_json_format)
    assert todos.add(test_data1["task"], test_data1["priority"]) == (
        test_data1["todo"],
        SUCCESS,
    )
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 1
