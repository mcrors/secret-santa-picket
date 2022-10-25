from app_config import AppConfig
from data_access.db_schema import DatabaseEngine, start_mappers


def bootstrap_repository(config: AppConfig):
    _ = DatabaseEngine.get_database_engine(config)
    start_mappers()

