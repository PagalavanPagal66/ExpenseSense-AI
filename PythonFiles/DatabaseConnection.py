import sqlite3
from Support import Transaction,TransactionB

def create_exp_table():
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Expenses (label TEXT, amount TEXT, tags TEXT)')
    conn.commit()
    c.close()
    return

def add_exp_data(transaction : Transaction):
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    label : str = transaction.label
    amount : int = transaction.value
    tags : list = transaction.category
    tag = ""
    for iter in tags:
        tag += iter
    print(label , amount , tag)
    c.execute('INSERT INTO Expenses (label, amount,tags) VALUES (?,?,?)',(label,amount, tag))
    conn.commit()
    c.close()

def delete_all_exp():
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    c.execute("DELETE FROM Expenses")
    conn.commit()
    c.close()

def get_all_exp():
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Expenses")
    li = c.fetchall()
    c.close()
    print(li)
    return li

def create_bud_table():
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Budget (label TEXT, amount TEXT)')
    conn.commit()
    c.close()
    return

def add_bud_data(transaction : TransactionB):
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    label : str = transaction.label
    amount : int = transaction.value
    print(label , amount)
    c.execute('INSERT INTO Budget (label, amount) VALUES (?,?)',(label,amount))
    conn.commit()
    c.close()

def delete_all_bud():
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    c.execute("DELETE FROM Budget")
    conn.commit()
    c.close()

def get_all_bud():
    conn = sqlite3.connect(r'C:\Project\ExpenseSense-AI\PythonFiles\Database\Database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Budget")
    li = c.fetchall()
    print(li)
    c.close()
    return li