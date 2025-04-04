import sqlite3
from pydantic.v1 import BaseModel
import DatabaseConnection as dbc

def run_sqlite_query():
    """Execute a SQLite query and fetch the results.

    Args:
        query: The SQL query to execute.

    Returns:
        A list of tuples containing the query results or an error message.
    """
    return ["Expenses","Budget"]
    conn = sqlite3.connect(r'Database/Database.db')
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

print(list_tables())
def describe_tables(table_name):
    with sqlite3.connect(r"Database\Database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+table_name+";")
        names = list(map(lambda x: x[0], cursor.description))
        print(names)
        return [names,cursor.fetchall()]

def get_str():
    tables = list_tables()
    print(tables)
    # budget = dbc.get_all_bud()
    # #print("All budget : ",budget)
    # expense = dbc.get_all_exp()
    # #print("All expense : ",expense)
    # budget_str = ""
    # it = 1
    # for iter in budget:
    #     budget_str += "\nBudget No : "+str(it)+" \n "
    #     budget_str += "Type of budget : "
    #     budget_str += iter[0]
    #     budget_str += "\nAmount of budget : "
    #     budget_str += iter[1]
    #     it += 1
    # it = 1
    # exp_str = ""
    # for iter in expense:
    #     exp_str += "Expense No : "+str(it)
    #     exp_str += "\n Type of expense : "
    #     exp_str += iter[0]
    #     exp_str += "\n Amount of budget : "
    #     exp_str += iter[1]
    #     exp_str += "\n categories of budget : "
    #     exp_str += iter[2]
    #     it += 1
    # print(budget_str+ " ------------- " + exp_str)
    # return budget_str + exp_str
    res = ""
    for iter in tables:
        #print(iter[0])
        res += "TABLE NAME : " + iter
        res += "\n TABLE CONTENT : \n"
        val = describe_tables(iter)
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
    if len(res):
        return res
    res = "No database entries found"
    print(res)
    return res
