import sqlite3

DB_NAME = 'newton.db'

def create_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """
        CREATE TABLE TASK (
            ID CHAR(100) PRIMARY KEY NOT NULL,
            FUNC CHAR(50)    NOT NULL,
            RESULT CHAR(50) NOT NULL
        );
        """
    )
    conn.close()

def insert(id, func, result):
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        f"""
        INSERT INTO TASK (ID, FUNC, RESULT) VALUES ('{id}', '{func}', '{result}');
        """
    )
    conn.commit()
    conn.close()
