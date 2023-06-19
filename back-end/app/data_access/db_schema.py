from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import registry

from app_config import AppConfig
from errors.secret_santa_exceptions import DatabaseNotConfiguredError
from models.user import User


metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("public_id", String, unique=True, nullable=False),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column('created_date', DateTime, nullable=False)
)


def start_mappers():
    mapper_registry = registry()
    _ = mapper_registry.map_imperatively(
        class_=User, local_table=users
    )


class DatabaseEngine:

    engine = None

    @classmethod
    def get_database_engine(cls, config: AppConfig = None) -> Engine:
        if cls.engine == None:
            if config == None:
                raise DatabaseNotConfiguredError()
            cls.engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        return cls.engine

