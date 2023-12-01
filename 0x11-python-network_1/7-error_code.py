#!/usr/bin/python3

"""
This script sends a request to the provided URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints the error code.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the body of the response
    print(response.text)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        # Print the error code
        print(f"Error code: {response.status_code}")
