from abc import ABC, abstractmethod

from src.infra.db.entities.users import Users as UsersEntity


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        pass

    @abstractmethod
    def select_user(self, first_name: str) -> list[UsersEntity] | None:
        pass
