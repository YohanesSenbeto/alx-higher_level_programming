#!/usr/bin/python3

"""
script sends that request to URL & displays the value of X-Request-Id variable found in response header.
"""


if __name__ == "__main__":
    import urllib.request
    import sys
      
    url = sys.argv[1]
    
    # Sending a request to the URL using urllib and a with statement
    with urllib.request.urlopen(url) as response:
        # Retrieving the value of the X-Request-Id variable from the response header
        x_request_id = response.getheader('X-Request-Id')
        
        print(x_request_id)
