from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.database import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    linked_accounts = Column(String, nullable=True)  # This should store encrypted link data

    def get_by_id(account_id: int):
        # Fetch account by ID from the database
        pass

    def get_by_email(email: str):
        # Fetch account by email from the database
        pass

    def save(self):
        # Save the account instance to the database
        pass