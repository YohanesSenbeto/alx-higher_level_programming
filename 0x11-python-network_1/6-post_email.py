#!/usr/bin/python3

"""
This script sends the POST request with an email parameter to the provided URL.
"""

import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request with the email parameter to the given URL.
    Retrieves the response body.
    """

    # Create payload with email parameter
    payload = {'email': email}

    # Send POST request with payload to the URL
    response = requests.post(url, data=payload)

    # Return the response body
    return response.text

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Print the email
    print(f"Your email is: {email}")

    # Send POST request and get response body
    response_body = send_post_request(url, email)

    # Print the response body
    print(response_body)
