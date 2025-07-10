from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    name: str
    attr1: float
    attr2: float
    attr3: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    score: float

    class Config:
        orm_mode = True

class WeightBase(BaseModel):
    attr1_weight: float
    attr2_weight: float
    attr3_weight: float

class WeightCreate(WeightBase):
    pass

class Weight(WeightBase):
    id: int

    class Config:
        orm_mode = True
