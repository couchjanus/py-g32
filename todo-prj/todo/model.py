from pathlib import Path

import json

from todo import JSON_ERROR, SUCCESS, DB_READ_ERROR, DB_WRITE_ERROR

class DBHandler:
    
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
    
    def read_todos(self):
        try:
            with self._db_path.open('r') as db:
                try:
                    return (json.load(db), SUCCESS)
                except json.JSONDecodeError:
                    return ([], JSON_ERROR)
        except OSError:
            return ([], DB_READ_ERROR)
        
    def write_todos(self, todo_list: []):
        try:
            with self._db_path.open('w') as db:
                json.dump(todo_list, db, indent=4)
            return (todo_list, SUCCESS)
        except OSError:
            return(todo_list, DB_WRITE_ERROR)
