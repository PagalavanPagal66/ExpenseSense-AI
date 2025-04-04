from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Support import Transaction,TransactionB
import DatabaseConnection as db
from typing import List
import BlockChain
app = FastAPI()

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

data = []

@app.get("/transactions")
async def get_func(transaction : Transaction):
    print(transaction)
    db.add_exp_data(transaction)
    data.append(transaction)
    return transaction

@app.post("/transactions")
async def post_func(transaction : Transaction):
    print(transaction)
    db.add_exp_data(transaction)
    my_chain.add_block(transaction)
    data.append(transaction)
    return transaction

@app.get("/return")
def get_ret():
    return db.get_all_exp()

@app.post("/return")
def post_ret():
    return db.get_all_exp()

@app.post("/deleteAll")
def post_del():
    data = []
    db.delete_all_exp()
    return data

@app.get("/deleteAll")
def get_del():
    data = []
    db.delete_all_exp()
    return data

@app.get("/transactionsB")
async def get_func(transaction : TransactionB):
    print(transaction)
    db.add_bud_data(transaction)
    data.append(transaction)
    return transaction

@app.post("/transactionsB")
async def post_func(transaction : TransactionB):
    print(transaction)
    my_chain.add_block(transaction)
    db.add_bud_data(transaction)
    data.append(transaction)
    return transaction

@app.get("/returnB")
def get_ret():
    return db.get_all_bud()

@app.post("/returnB")
def post_retB():
    return db.get_all_bud()

@app.post("/deleteAllB")
def post_delB():
    data = []
    db.delete_all_bud()
    return data

@app.get("/deleteAllB")
def get_delB():
    data = []
    db.delete_all_bud()
    return data

my_chain = BlockChain.Blockchain()

if __name__ == '__main__':
    db.create_exp_table()
    db.create_bud_table()

    uvicorn.run(app, host='localhost', port=8001)