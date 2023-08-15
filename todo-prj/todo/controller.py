"""This module provides the TODO controller."""
from pathlib import Path

from todo.model import DBHandler
from todo import DB_READ_ERROR

class Todo:
    todo = {
        'Task': '',
        'Priority': 2,
        'Done': False
    }
    
    # todo_list: []
    
    db_path: Path 
    
    def __init__(self, db_path: Path) -> None:
        self.todo_list = []
        self._db_handler = DBHandler(db_path)
        
    # def my_method (self):
    #     print(f"Class attribute todo: {self.todo}")
    
    def add(self, task: [], priority: int = 2):
        """Add a new todo to database."""
        task_description = " ".join(task)
        
        if not task_description.endswith('.'):
            task_description += '.'
            
        self.todo = {
            'Task': task_description,
            'Priority': priority,
            'Done': False 
        }
        
        self.todo_list, read_error = self._db_handler.read_todos()
        if read_error == DB_READ_ERROR:
            return (self.todo, read_error)
        
        self.todo_list.append(self.todo)
        
        self.todo_list, write_error = self._db_handler.write_todos(self.todo_list)
        
        return (self.todo, write_error)
        
        
    


if __name__ == "__main__":
    test_todo = Todo()
    
    # print(test_todo)
    # print(type(test_todo))
    # print(dir(test_todo))
    # print(test_todo.__dict__)
    # print(Todo.__dict__)
    # print(Todo.__annotations__)
    # test_todo.my_method()
    
    
    
    
    
