#!/usr/bin/env python3
"""
Module that creates a BasicAuth Class
"""
import base64
from models.user import User
import logging
from api.v1.auth.auth import Auth
from typing import TypeVar

logging.basicConfig(filename='app.log', filemode='a')


class BasicAuth(Auth):
    """The Basic Auth class BP
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the base64 part of Authorization header
        """
        # Check if the authorization_header is a string and well-formed
        if not isinstance(authorization_header, str) or \
                not authorization_header.startswith("Basic "):
            return None

        # Split the authorization_header into parts
        parts = authorization_header.split()

        # Check if the Authorization header is well-formed
        if len(parts) != 2:
            return None

        # Extract and return the base64 part (the second part after splitting)
        return parts[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of Base64 string
        Args:
            base64_authorization_header - Header
        Returns
            decoded value
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.urlsafe_b64decode(
                base64_authorization_header).decode('utf-8')

        except (TypeError, ValueError) as e:
            logging.warning(f"Erro decoding base64: {e}")
            return None
        return decoded_value

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Returns a tuple of username and password from a decoded base64 value
        """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if decoded_base64_authorization_header.find(':') < 0:
            return (None, None)
        credentials = decoded_base64_authorization_header.partition(':')
        return (credentials[0], credentials[-1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns a user instance based on email and password
        Args:
            user_email  (str) - email
            user_pwd (str) - password
        Returns:
            user_object
        """
        # Check if user_email or user_pwd is not a string or None
        if not isinstance(user_email, str) or user_email is None:
            return None
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None

        # Search for user in the database
        users = User.search({"email": user_email})

        # If user not found, return None
        if not users:
            return None

        # If multiple users found, log a warning and return None
        if len(users) > 1:
            print("Warning: Multiple users found with the same email.")
            return None

        user = users[0]  # Get the first user from the list

        # Check if provided password is valid
        if not user.is_valid_password(user_pwd):
            return None

        # Return the user instance if authentication is successful
        return user
