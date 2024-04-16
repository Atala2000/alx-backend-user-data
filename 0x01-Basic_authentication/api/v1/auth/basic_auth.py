#!/usr/bin/env python3
"""
Module that creates a BasicAuth Class
"""


from api.v1.auth.auth import Auth
class BasicAuth(Auth):
    """The Basic Auth class BP
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Returns the base64 part of Authorization header
        """
        # Check if the authorization_header is a string and well-formed
        if not isinstance(authorization_header, str) or not authorization_header.startswith("Basic "):
            return None
        
        # Split the authorization_header into parts
        parts = authorization_header.split()

        # Check if the Authorization header is well-formed
        if len(parts) != 2:
            return None

        # Extract and return the base64 part (the second part after splitting)
        return parts[1]