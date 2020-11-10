import os

SECRET_KEY = os.getenv('SECRET_KEY', 'chave_de_seguranca')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./todo.db')