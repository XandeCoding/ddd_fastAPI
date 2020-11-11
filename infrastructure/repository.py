import databases
import sqlalchemy
import environment

database = databases.Database(environment.DATABASE_URL)
metadata = sqlalchemy.MetaData()

todosTable = sqlalchemy.Table(
    "todos",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('text', sqlalchemy.String),
    sqlalchemy.Column('completed', sqlalchemy.Boolean)
)

engine = sqlalchemy.create_engine(
    environment.DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
