from .database import Base, engine, SessionLocal
from . import models


def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    if not db.query(models.Item).first():
        items = [
            models.Item(name="Item A", attr1=5, attr2=3, attr3=8),
            models.Item(name="Item B", attr1=2, attr2=9, attr3=1),
            models.Item(name="Item C", attr1=7, attr2=4, attr3=5),
        ]
        db.add_all(items)
        db.add(models.Weight(attr1_weight=1.0, attr2_weight=1.0, attr3_weight=1.0))
        db.commit()
    db.close()
