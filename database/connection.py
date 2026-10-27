from sqlmodel import SQLModel, Session, create_engine
from models.events import Event  # Обязательно для создания таблицы

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}

engine_url = create_engine(
    database_connection_string,
    echo=True,
    connect_args=connect_args,
)

def conn():
    """Создает файл БД и таблицы"""
    SQLModel.metadata.create_all(engine_url)

def get_session():
    """Дает сессию для работы с БД"""
    with Session(engine_url) as session:
        yield session