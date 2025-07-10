from sqlalchemy import Column, Integer, String, Float

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    attr1 = Column(Float)
    attr2 = Column(Float)
    attr3 = Column(Float)

class Weight(Base):
    __tablename__ = "weights"

    id = Column(Integer, primary_key=True, index=True, default=1)
    attr1_weight = Column(Float, default=1.0)
    attr2_weight = Column(Float, default=1.0)
    attr3_weight = Column(Float, default=1.0)
