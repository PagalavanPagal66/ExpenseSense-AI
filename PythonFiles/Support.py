from pydantic import BaseModel
from enum import Enum
from typing import Optional,List

class Transaction(BaseModel):
    value : str
    label : str
    category : List[str]
