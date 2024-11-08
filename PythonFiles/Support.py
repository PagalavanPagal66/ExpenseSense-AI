from pydantic import BaseModel
from enum import Enum
from typing import Optional,List

class Transaction(BaseModel):
    value : int
    label : str
    category : List[str]

class TransactionB(BaseModel):
    value : int
    label : str
