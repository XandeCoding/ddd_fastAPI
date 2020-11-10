from pydantic import BaseModel

class TodoIn(BaseModel):
    text: str
    completed: bool

class Todo(BaseModel):
    id: int
    text: str
    completed: bool