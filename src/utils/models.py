from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import INTEGER, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: Member Model for Leveling


class Member(Base):
    __tablename__ = "member"
    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(TEXT)
    avatar = Column(TEXT)
