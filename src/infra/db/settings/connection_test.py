import pytest

from .connection import DbConnectionHandler


# uv run pytest -s -v
@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DbConnectionHandler()

    engine = db_connection_handle.get_engine()

    assert engine is not None

    # conn = engine.connect()
    # print()
    # print()
    # print()
    # print()
    # print("conn >>>>>> ", conn)

    # conn.execute(
    #     text("INSERT INTO USERS (first_name, last_name, age) VALUES ('Ola', 'mundo', 123)")
    # )

    # conn.commit()
