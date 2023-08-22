import pytest
import json

from todo import (
    controller,
    SUCCESS
)

# content of test_tmp_path.py
CONTENT = "content"


# def test_create_file(tmp_path):
#     d = tmp_path / "sub"
#     d.mkdir()
#     p = d / "hello.txt"
#     p.write_text(CONTENT)
#     assert p.read_text() == CONTENT
#     assert len(list(tmp_path.iterdir())) == 1
#     assert 0
    
@pytest.fixture
def mock_json_file(tmp_path):
   todo = [{"Task": "Get some milk.", "Priority": 2, "Done": False}]
   
   # d.mkdir()
   db_file = tmp_path / "todo.json"
   # db_file.touch()
   with db_file.open("w+") as db:
       json.dump(todo, db, indent=4)
   return db_file

@pytest.fixture
def mocking_json_file(tmp_path):
    todo = [{"Task": "Get something there.", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file
    

def test_add_task_success(mock_json_file):
    todos = controller.Todo(mock_json_file)
    result = todos.add(["Put something there."], 1)
    assert result.error == SUCCESS
    result = todos.add(["Put other there."], 3)
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 2

# def test_add_task_success(mock_json_file):
#    todos = controller.Todo(mock_json_file)
#    result = todos.add("Put some milk.", 1)
#    assert result.error == SUCCESS
#    read = todos._db_handler.read_todos()
#    assert len(read.todo_list) == 2

CONTENT = "content"


# def test_create_file(tmp_path):
#     d = tmp_path / "sub"
#     d.mkdir()
#     p = d / "hello.txt"
#     p.write_text(CONTENT)
#     assert p.read_text() == CONTENT
#     assert len(list(tmp_path.iterdir())) == 1
    # assert 0