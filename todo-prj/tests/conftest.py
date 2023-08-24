# content of conftest.py
import pytest
import json
# 
@pytest.fixture
def mock_json_file(tmp_path):
    todo = [{"Task": "Get some milk.", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file

@pytest.fixture
def mock_wrong_json_file(tmp_path):
    db_file = tmp_path / "todo.json"
    return db_file

@pytest.fixture
def mock_wrong_json_format(tmp_path):
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        db.write("")
    return db_file

