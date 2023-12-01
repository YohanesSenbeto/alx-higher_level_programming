#!/usr/bin/python3
"""
This script fetches the status from 'https://alx-intranet.hbtn.io/status' using urllib.
"""
from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Fetching the URL using urllib and using a with statement
    with request.urlopen(url) as response:
        # Reading the response body
        body = response.read()
        
        # Decoding the response body using utf-8
        utf8_content = body.decode('utf-8')
        
        # Displaying the body of the response with tabulation before each line
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {utf8_content}")
