#!/usr/bin/env python3
"""
Module that creates a user class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Model for a user class
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    hashed_password = Column(String(50), nullable=False)
    session_id = Column(String(50), nullable=True)
    reset_token = Column(String(50), nullable=True)
