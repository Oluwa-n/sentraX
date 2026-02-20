 # SQLAlchemy models:
  # - User
   # - Conversation
  # - Model
  # - Plan
   # - UsageLog
  # Structure only. No logic.
  
  
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# Users Table
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    
    telegram_id = Column(String, unique=True, index=True)
    
    username = Column(String)
    
    plan_id = Column(Integer, ForeignKey("plans.id"))
    
    balance_tokens = Column(Float, default=10.0)
    
    is_active = Column(Integer, default=1)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    plan = relationship("Plan", back_populates="users")
    
    conversations = relationship("Conversation", back_populates="user")
    
    usage_logs = relationship("UsageLog", back_populates="user")
    
    prompts = relationship("Prompt", back_populates="user")
    
    AIModel = relationship("AIModel", back_populates="users")


# Plans Table
class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, unique=True)
    
    monthly_tokens = Column(Float, default=10)
    
    daily_limit = Column(Integer, default=5)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", back_populates="plan")


# Usage Logs Table
class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    
    action_type = Column(String)  # ai_basic / ai_advanced / osint
    
    input_tokens = Column(Float, nullable=True)
    
    output_tokens = Column(Float, nullable=True)
    
    total_tokens = Column(Float, nullable=True)
    
    cost = Column(Float, default=0.0)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="usage_logs")


# Conversations Table
class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    
    model_used = Column(String)
    
    user_message = Column(String)
    
    ai_response = Column(String)
    
    total_tokens = Column(Float, default=0.0)
    
    cost = Column(Float, default=0.0)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="conversations")
    
    
class AIModel(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, unique=True)
    
    version = Column(String, nullable=True)
    
    description = Column(String, nullable=True)
    
    token_cost = Column(Float, default=0.5)  # cost per token for this model
    
    is_active = Column(Integer, default=1)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    users = relationship("User", back_populates="AIModel")

    
    
class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # null = default prompt
    
    name = Column(String)
    
    content = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="prompts")


