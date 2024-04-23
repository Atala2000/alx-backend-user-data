#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Method that saves a user to a database

        Args:
            email (str): Email of the user
            hashed_password (str): The password of the user after hashing

        Returns:
            : User object
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            user = None
        return user

    def find_user_by(self, **kwargs):
        """
        Filters row by multiple arguments
        """
        try:
            # Perform the query with the provided filter criteria
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound as e:
            # If no user is found, raise NoResultFound
            raise NoResultFound("No user found matching the filter criteria.") from e
        except InvalidRequestError as e:
            # If wrong query arguments are passed, raise InvalidRequestError
            raise InvalidRequestError("Wrong query arguments.") from e
