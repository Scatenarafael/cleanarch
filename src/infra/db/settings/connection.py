from sqlalchemy import create_engine


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "postgresql+psycopg2", 
            "postgres", 
            "postgres", 
            "localhost", 
            "5433", 
            "clean_arch_db"
            )
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
        