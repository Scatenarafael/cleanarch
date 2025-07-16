from src.data.usecases.user_finder import UserFinder
from src.infra.db.repositories.users_repository import UsersRepository


def test_find():
    repository = UsersRepository()
    user_finder = UserFinder(repository)
