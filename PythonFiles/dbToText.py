import sqlite3
from pydantic.v1 import BaseModel

def run_sqlite_query():
    """Execute a SQLite query and fetch the results.

    Args:
        query: The SQL query to execute.

    Returns:
        A list of tuples containing the query results or an error message.
    """
    with sqlite3.connect(r"C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            return cursor.fetchall()
        except sqlite3.OperationalError as err:
            return f"The following error occurred: {str(err)}"

class RunQueryArgsSchema(BaseModel):
    query: str

def list_tables():
    rows = run_sqlite_query()
    return rows


def describe_tables(table_name):
    with sqlite3.connect(r"C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+table_name+";")
        return cursor.fetchall()

def get_str():
    tables = list_tables()
    print(type(tables))
    res = " TABLE NAME : "
    for iter in tables:
        print(iter[0])
        res += iter[0]
        res += "\n TABLE CONTENT : \n"
        val = describe_tables(iter[0])
        for i in range(0,len(val)):
            res+="ROW "+i
            res+=val[i]
        res += "\n"
    print(res)

get_str()

