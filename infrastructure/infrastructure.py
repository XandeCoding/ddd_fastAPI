from fastapi import FastAPI
from modules.todos import todos
from repository import repository

app = FastAPI()

@app.on_event('startup')
async def startup():
    await repository.database.connect()

@app.on_event('shutdown')
async def shutdown():
    await repository.database.disconnect()


app.mount('/todos', todos.todoApp)
