#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response, handling HTTP errors.
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    # Checking if a URL is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        # Sending a request to the URL using urllib and a with statement
        with request.urlopen(url) as response:
            # Reading and decoding the body of the response
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        # Handling HTTP errors
        print(f"Error code: {e.code}")
