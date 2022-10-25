import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session, clear_mappers

from app_config import AppConfig
from data_access.db_schema import start_mappers, metadata, DatabaseEngine
from main import make_app
from models.user import User



@pytest.fixture
def app_config():
    return AppConfig()


@pytest.fixture
def app():
    return make_app()


@pytest.fixture
def engine(app_config) -> Engine:
    return DatabaseEngine.get_database_engine(app_config)


@pytest.fixture
def engine_with_schema(engine: engine):
    start_mappers()
    metadata.create_all(engine)
    yield engine
    clear_mappers()
    metadata.drop_all(engine)


@pytest.fixture
def engine_with_schema_and_multiple_users(engine_with_schema):
    session = Session(engine_with_schema)
    session.add_all(_list_of_users())
    session.flush()
    session.commit()
    yield


@pytest.fixture
def session(engine_with_schema: Engine):
    session = Session(engine_with_schema)
    yield session
    session.close()


def _list_of_users():
    return [
        User('Tony', 'Soprano', 'ts@badabing.com'),
        User('Johnny', 'Cash', 'jc@folsomprison.com'),
        User('Serena', 'Williams', 'sw@tennis.com')
    ]

