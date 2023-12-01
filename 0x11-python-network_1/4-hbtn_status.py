#!/usr/bin/python3
"""
This script sends a GET request to 'https://alx-intranet.hbtn.io/status'
and displays information about the response content.
"""

import requests

if __name__ == "__main__":
    # Define the URL
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the response body
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

