from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format("postgresql+psycopg2", "postgres", "postgres", "localhost", "5433", "clean_arch_db")
        self.__engine = self.__create_database_engine()
        self.session: Session | None = None

    def __create_database_engine(self) -> Engine:
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self) -> Engine:
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
