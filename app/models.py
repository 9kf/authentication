from .config.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, func

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    profile_picture = Column(String)
    created_at = Column(TIMESTAMP(timezone=True,), server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())