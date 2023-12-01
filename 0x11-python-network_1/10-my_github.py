#!/usr/bin/python3

"""
This script takes the GitHub credentials (username and personal access token) and uses the GitHub API
to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    # Get username and password from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send GET request to GitHub API with authentication
    response = requests.get(
        'https://api.github.com/user',
        auth=(username, password)
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        user_data = response.json()
        # Extract the user's id from the response
        user_id = user_data['id']
        # Print the user's id
        print(user_id)
    else:
        # Print None if the request was not successful
        print(None)
