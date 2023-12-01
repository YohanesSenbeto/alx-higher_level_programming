#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from command line argument
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if X-Request-Id is present in the response headers
    if 'X-Request-Id' in response.headers:
        # Display the value of X-Request-Id
        print(response.headers['X-Request-Id'])
    else:
        print("X-Request-Id header not found in the response.")
