from sqlalchemy.orm import Session
import schema, models


def create_user(db: Session, user: schema.User):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        return error_message('User already exists')
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def delete_user(db: Session, username: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

def create_house(db: Session, house: schema.Houses):
    db_house = db.query(models.Houses).filter(models.Houses.id == house.id).first()
    if db_house:
        return error_message('House already exists')
    db_house = models.Houses(**house.dict())
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

def get_houses(db: Session, house_id: int = None):
    return db.query(models.Houses).all() if house_id is None else db.query(models.Houses).filter(models.Houses.id == house_id).first()

def delete_house(db: Session, house_id: int):
    db_house = db.query(models.Houses).filter(models.Houses.id == house_id).first()
    if db_house:
        db.delete(db_house)
        db.commit()
        return True
    return False

def error_message(message: str):
    return {'error': message}