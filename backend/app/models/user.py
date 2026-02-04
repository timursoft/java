from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4

class Invitation(Base):
    __tablename__ = 'invitations'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    referral_link = Column(String, nullable=False, unique=True)
    invited_by_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    invited_on = Column(DateTime, default=datetime.utcnow)

    invited_by_user = relationship('User', back_populates='invitations')

    def generate_referral_link(self):
        """Generate a unique referral link using UUID."""
        self.referral_link = f"https://example.com/invite/{uuid4()}"

User.invitations = relationship('Invitation', order_by=Invitation.id, back_populates='invited_by_user')