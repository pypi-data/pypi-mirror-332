# http.py
# v0.3.0

"""HTTP Utility Functions"""

#region Imports

import requests

from typing import List, Optional

from ..decorators import retry_http

#endregion

#region Exports

__all__: List[str] = [
    'get_with_retry',
]

#endregion

#region Functions

@retry_http
def get_with_retry(
            url: str,
            *,
            session: Optional[requests.Session],
        ) -> requests.Response:

    """Helper function to perform a simple GET web request with retries.

    :param url: The URL to fetch.
    :type url: str

    :param session: An optional `requests.Session` object
        to use for the request.
    
    :return: A `requests.Response`.
    :rtype: requests.Response
    """
    if session:
        return session.get(url)
    
    else:
        return requests.get(url)

#endregion
