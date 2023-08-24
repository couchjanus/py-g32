# test_add_wrong_json_file.py
import json
import pytest

from todo import (
    DB_READ_ERROR,
    controller,
)

@pytest.fixture
def mock_wrong_json_file(tmp_path):
    db_file = tmp_path / "todo.json"
    return db_file


def test_add_wrong_json_file(mock_wrong_json_file):
    todos = controller.Todo(mock_wrong_json_file)
    response = todos.add(["test task"], 1)
    assert response.error == DB_READ_ERROR
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 0
