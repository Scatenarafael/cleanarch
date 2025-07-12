import pytest
from sqlalchemy import text

from src.infra.db.settings.connection import DbConnectionHandler

from .users_repository import UsersRepository

db_connection_handler = DbConnectionHandler()

connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 34

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = """
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = {}
    """.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(
        text(f"""
                            DELETE FROM users WHERE id = {registry.id}
                            """)
    )

    connection.commit()


def test_select_user():
    mocked_first_name = "first_2"
    mocked_last_name = "last_2"
    mocked_age = 34

    sql = """
        INSERT INTO users (first_name, last_name, age) VALUES ('{}','{}','{}')
    """.format(mocked_first_name, mocked_last_name, mocked_age)

    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()

    response = users_repository.select_user(mocked_first_name)

    assert response is not None and len(response) > 0, "No user found in response"
    user = response[0]
    assert getattr(user, "first_name", None) == mocked_first_name
    assert getattr(user, "last_name", None) == mocked_last_name
    assert getattr(user, "age", None) == mocked_age

    connection.execute(
        text(f"""
                            DELETE FROM users WHERE id = {user.id}
                            """)
    )

    connection.commit()
