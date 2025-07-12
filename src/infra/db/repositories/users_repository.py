from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DbConnectionHandler


class UsersRepository:
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DbConnectionHandler() as database:
            try:
                new_registry = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                if database.session:
                    database.session.add(new_registry)
                    database.session.commit()
            except Exception as exception:
                if database.session:
                    database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> list[UsersEntity] | None:
        with DbConnectionHandler() as database:
            try:
                if database.session:
                    users = database.session.query(UsersEntity).filter(UsersEntity.first_name == first_name).all()
                    return users
            except Exception as exception:
                if database.session:
                    database.session.rollback()
                raise exception
