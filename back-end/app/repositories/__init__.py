from app_config import AppConfig
from data_access.db_schema import DatabaseEngine, metadata, start_mappers


def bootstrap_repository(config: AppConfig):
    engine = DatabaseEngine.get_database_engine(config)
    metadata.create_all(engine)
    start_mappers()

