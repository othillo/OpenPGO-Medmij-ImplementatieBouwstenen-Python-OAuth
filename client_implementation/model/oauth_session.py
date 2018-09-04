import datetime
import uuid

from sqlalchemy import Column
from sqlalchemy.types import (
    DateTime,
    Text,
    Boolean
)

from . import Base

class OAuthSession(Base):
    """OAuthSession model"""
    __tablename__ = 'oauth_sessions'

    id = Column(Text, primary_key=True)
    state = Column(Text)
    scope = Column(Text)
    za_name = Column(Text)
    authorization_code = Column(Text)
    authorized = Column(Boolean)
    access_token = Column(Text)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, za_name, state):
        self.id = str(uuid.uuid4())
        self.state = state
        self.scope = '1'
        self.za_name = za_name
        self.authorization_code = None
        self.authorized = False
        self.access_token = None
        self.created_at = datetime.datetime.now()