#!/usr/bin/env python3
"""
Module that creates a BasicAuth Class
"""
import base64
import logging
from api.v1.auth.auth import Auth

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
