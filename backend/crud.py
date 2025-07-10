from sqlalchemy.orm import Session

from . import models, schemas

def get_weights(db: Session):
    return db.query(models.Weight).first()


def set_weights(db: Session, weights: schemas.WeightCreate):
    obj = get_weights(db)
    if obj is None:
        obj = models.Weight(**weights.dict())
        db.add(obj)
    else:
        obj.attr1_weight = weights.attr1_weight
        obj.attr2_weight = weights.attr2_weight
        obj.attr3_weight = weights.attr3_weight
    db.commit()
    db.refresh(obj)
    return obj


def get_items(db: Session):
    weight = get_weights(db)
    if weight is None:
        weight = models.Weight(attr1_weight=1.0, attr2_weight=1.0, attr3_weight=1.0)
        db.add(weight)
        db.commit()
    items = db.query(models.Item).all()
    res = []
    for item in items:
        score = (
            weight.attr1_weight * item.attr1
            + weight.attr2_weight * item.attr2
            + weight.attr3_weight * item.attr3
        )
        res.append((item, score))
    res.sort(key=lambda x: x[1], reverse=True)
    return [schemas.Item(id=it.id, name=it.name, attr1=it.attr1, attr2=it.attr2, attr3=it.attr3, score=sc) for it, sc in res]


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
