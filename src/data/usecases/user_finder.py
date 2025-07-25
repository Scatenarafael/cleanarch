from typing import Dict

from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        raise NotImplementedError
