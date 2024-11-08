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
        names = list(map(lambda x: x[0], cursor.description))
        return [names,cursor.fetchall()]

def get_str():
    tables = list_tables()
    #print(tables)
    res = ""
    for iter in tables:
        #print(iter[0])
        res += "TABLE NAME : " + iter[0]
        res += "\n TABLE CONTENT : \n"
        val = describe_tables(iter[0])
        ref = val[0]
        rows = val[1:]
        ctr=0
        rows = rows[0]
        for row in rows:
            ctr+=1
            res+="ROW "+str(ctr)+" : "
            ind = 0
            #print(row)
            for entry in row:
                res+="( "+ref[ind]+" - " + str(entry)+ " ) , "
                ind+=1
        res += "\n"
    print(res)
    return res

