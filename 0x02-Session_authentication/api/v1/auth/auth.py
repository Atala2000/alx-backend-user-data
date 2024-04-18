#!/usr/bin/env python3
"""
Module for creating authenitcation
"""
from flask import request
import os
from typing import List, TypeVar


class Auth:
    """
    Class to create authentication objects
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns true if path is allowed
        """
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        if not request:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """returns None"""
        return None

    def session_cookie(self, request=None):
        """
        Method that returns a cookie value from a  request

        Args
            request (str): The request header

        Returns:
            str: Cookie value
        """
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(cookie_name)
