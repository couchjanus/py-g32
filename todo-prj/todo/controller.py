"""This module provides the TODO controller."""
from pathlib import Path

from todo.model import DBHandler
from todo import DB_READ_ERROR, ID_ERROR
from typing import List, Dict, Any

from todo.aliases import TodoList
from todo.todo_response import TodoResponse
from todo.todo_item import TodoItem

class Todo:

    db_path: Path 
    todo: TodoItem
     
    def __init__(self, db_path: Path) -> None:
        self.todo_list = []
        self._db_handler = DBHandler(db_path)
        self.todo = TodoItem()
        
    def add(self, task: [], priority: int = 2)->TodoResponse:
        """Add a new todo to database."""
        task_description = " ".join(task)
        
        if not task_description.endswith('.'):
            task_description += '.'
            
        self.todo = {
            'Task': task_description,
            'Priority': priority,
            'Done': False 
        }
        
        read = self._db_handler.read_todos()
        if read.error == DB_READ_ERROR:
            return TodoResponse(self.todo, read.error)
        
        self.todo_list.append(self.todo)
        
        write = self._db_handler.write_todos(self.todo_list)
        
        return TodoResponse(self.todo, write.error)
        
    # def get_todo_list(self)->List[Dict[str, Any]]:
    def get_todo_list(self)->TodoList:
        """Return the current todo list."""
        read = self._db_handler.read_todos()
        return read.todo_list
    
    def remove(self, todo_id: int) -> TodoResponse:
        """Remove a todo from database using its id or index."""
        read = self._db_handler.read_todos()
        if read.error:
            return TodoResponse({}, read.error)
        try:
            self.todo = read.todo_list.pop(todo_id - 1)
        except IndexError:
            return TodoResponse({}, ID_ERROR)
        write = self._db_handler.write_todos(read.todo_list)
        return TodoResponse(self.todo, write.error)


if __name__ == "__main__":
    test_todo = Todo()
    
    # print(test_todo)
    # print(type(test_todo))
    # print(dir(test_todo))
    # print(test_todo.__dict__)
    # print(Todo.__dict__)
    # print(Todo.__annotations__)
    # test_todo.my_method()
    
    
    
    
    
