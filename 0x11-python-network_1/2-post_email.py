#!/usr/bin/python3

"""
This script sends a POST request to a given URL with an email as a parameter and displays the body of the response.
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    # Checking if the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: ./script_name.py <URL> <email>")
        sys.exit(1)
    
    # Extracting URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Encoding the email parameter
    data = parse.urlencode({'email': email})
    data = data.encode('utf-8')  # Encoding the data to bytes
    
    # Sending a POST request to the URL with the email as a parameter using urllib and a with statement
    with request.urlopen(url, data) as response:
        # Reading and decoding the body of the response
        body = response.read().decode('utf-8')
        print(body)
