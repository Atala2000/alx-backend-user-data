#!/usr/bin/env python3
"""
Module for creating authenitcation
"""
from flask import request
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
