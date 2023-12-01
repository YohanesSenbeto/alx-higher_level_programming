#!/usr/bin/python3

"""
script sends a POST request to a given URL with an email as a parameter & displays the body of the response.
"""


if __name__ == "__main__":
    from urllib.request import urlopen,Request
    from urllib.parse import urlencode
    from sys import argv
    
    # Encoding the email parameter
    value = parse.urlencode({'email': email})
    request = Request(
            argv[1], urlencode(value).encode("ascii"))
    
    # Sending a POST request to the URL with the email as a parameter using urllib and a with statement
    with urlopen(request) as response:
        # Reading and decoding the body of the response
        body = response.headers.get('x-Request-id')
        print(response.read().decode('utf-8'))
