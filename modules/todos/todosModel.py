from repository import repository
from modules.todos import todosSchema

class TodosModel:
    todosTable = repository.todosTable

    @staticmethod
    async def getAllTodos():
        query = repository.todosTable.select()
        return await repository.database.fetch_all(query)

    @staticmethod
    async def addTodo(todo: todosSchema.TodoIn):
        query = repository.todosTable.insert().values(
            text=todo.text,
            completed=todo.completed
        )
        last_record_id = await repository.database.execute(query)
        return { ** todo.dict(), "id": last_record_id }