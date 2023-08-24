# test_add_task_to_json_file.py

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

test_data2 = {
    "task": ["Wash the car"],
    "priority": 2,
    "todo": {
        "Task": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}


@pytest.mark.parametrize(
    "task, priority, expected",
    [
        pytest.param(
            test_data1["task"],
            test_data1["priority"],
            (test_data1["todo"], SUCCESS),
        ),
        pytest.param(
            test_data2["task"],
            test_data2["priority"],
            (test_data2["todo"], SUCCESS),
        ),
    ],
)
def test_add_task_to_json_file(mock_json_file, task, priority, expected):
    todos = controller.Todo(mock_json_file)
    assert todos.add(task, priority) == expected
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 2
