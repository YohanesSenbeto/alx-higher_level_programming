#!/usr/bin/python3

"""
This script sends that request to a URL and displays the value of the X-Request-Id variable found in the response header.
"""

from urllib import request
import sys

if __name__ == "__main__":
    # Checking if a URL is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: ./script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Sending a request to the URL using urllib and a with statement
    with request.urlopen(url) as response:
        # Retrieving the value of the X-Request-Id variable from the response header
        x_request_id = response.getheader('X-Request-Id')
        
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
