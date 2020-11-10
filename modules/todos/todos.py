from fastapi import FastAPI
from typing import List
from modules.todos.todosSchema import Todo, TodoIn
from modules.todos.todosModel import TodosModel

todoApp = FastAPI()

@todoApp.get('/getAll', response_model=List[Todo])
async def getAllTodos():
    return await TodosModel.getAllTodos()

@todoApp.post('/add', response_model=Todo)
async def addTodo(todo: TodoIn):
    return await TodosModel.addTodo(todo)