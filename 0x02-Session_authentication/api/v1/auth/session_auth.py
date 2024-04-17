#!/usr/bin/env python3
"""
Module that creates Session Authentication
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    Session Auth Class blueprint empty for now

    Attributes

    -------
    user_id_by_session_id : dict
        dict that contains session id and user id
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session id for a user

        Args:
            user_id (str, optional): The user_id to use

        Returns:
            str: a string that represents a session id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
