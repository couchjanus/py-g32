from typing import TypedDict

class TodoItem(TypedDict):
    Task: str
    Priority: int
    Done: bool