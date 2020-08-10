import sqlite3

DB_NAME = 'newton.db'


def create_table(id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute(f"DROP TABLE IF EXISTS SERVER_{id};")
    conn.execute(
        f"""
        CREATE TABLE SERVER_{id} (
            ID CHAR(100) PRIMARY KEY NOT NULL,
            FUNC CHAR(50)    NOT NULL,
            RESULT CHAR(50) NOT NULL
        );
        """
    )
    conn.close()


def insert(server, id, func, result):
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        f"""
        INSERT INTO SERVER_{server} (ID, FUNC, RESULT) VALUES ('{id}', '{func}', '{result}');
        """
    )
    conn.commit()
    conn.close()


def select(id):
    conn = sqlite3.connect(DB_NAME)

    query = conn.execute(f"SELECT ID, FUNC, RESULT FROM SERVER_{id}")
    query = [list(row) for row in query]

    conn.close()
    return query
