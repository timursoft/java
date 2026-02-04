from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Regulation(Base):
    __tablename__ = 'regulations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    country = Column(String, nullable=False)
    applicability_criteria = Column(String)

    def __repr__(self):
        return f"<Regulation(name='{self.name}', country='{self.country}')>"