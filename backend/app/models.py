from sqlalchemy.orm import relationship, joinedload
from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.db.base_class import Base

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    parent = relationship("Parent", back_populates="children")

    def fetch_with_eager_loading(self):
        """Fetch using SQLAlchemy's eager loading to avoid N+1 query issues."""
        return session.query(Parent).options(joinedload(Parent.children)).all()
