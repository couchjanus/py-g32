import json
import pytest

from todo import (
    SUCCESS,
    controller,
)


@pytest.fixture
def mocking_json_file(tmp_path):
    todo = [{"Task": "Get some milk.", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file

def test_add_task_success(mocking_json_file):
    todos = controller.Todo(mocking_json_file)
    result = todos.add("Put some milk.", 1)
    assert result.error == SUCCESS
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 2
