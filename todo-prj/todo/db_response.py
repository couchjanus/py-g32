from todo.aliases import TodoList
from typing import NamedTuple

class DBResponse(NamedTuple):
    todo_list: TodoList
    error: int
