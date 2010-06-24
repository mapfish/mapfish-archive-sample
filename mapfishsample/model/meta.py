"""SQLAlchemy Metadata and Session object"""
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__all__ = ['Session', 'Base']

# SQLAlchemy session manager.  Updated by model.init_model()
Session = scoped_session(sessionmaker())

# The declarative Base
Base = declarative_base()
