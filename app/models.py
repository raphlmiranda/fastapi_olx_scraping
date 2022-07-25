from database import Base
from sqlalchemy import Column, ForeignKey, String, Integer


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(username='{self.username}')>"


class Houses(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key = True, autoincrement = True)
    description = Column(String)
    price = Column(String)
    rooms = Column(String)
    area = Column(String)
    tax = Column(String)
    date = Column(String)
    user = Column(ForeignKey('users.id'), nullable = False)