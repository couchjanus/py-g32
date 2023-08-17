from todo.aliases import TodoDict
from typing import NamedTuple

class TodoResponse(NamedTuple):
    todo_list: TodoDict
    error: int
