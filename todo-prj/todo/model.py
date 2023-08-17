from pathlib import Path

import json

from todo import JSON_ERROR, SUCCESS, DB_READ_ERROR, DB_WRITE_ERROR
from todo.db_response import DBResponse
from todo.aliases import TodoList

class DBHandler:
    
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
    
    def read_todos(self)->DBResponse:
        try:
            with self._db_path.open('r') as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:
                    return DBResponse([], JSON_ERROR)
        except OSError:
            return DBResponse([], DB_READ_ERROR)
        
    def write_todos(self, todo_list: TodoList)->DBResponse:
        try:
            with self._db_path.open('w') as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
        except OSError:
            return DBResponse(todo_list, DB_WRITE_ERROR)
