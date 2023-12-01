#!/usr/bin/python3

"""
This script takes in a letter &  sends a POST request to http://0.0.0.0:5000/search_user.
It displays the response in a specific format based on the JSON content received.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if a letter is provided as command line argument
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    # Create data dictionary with the letter
    data = {'q': q}

    # Send POST request to the server
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        # Convert response to JSON
        json_response = response.json()

        # Check if JSON response is not empty
        if json_response:
            # Print the ID and name from the JSON response
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            # Print message if no result found
            print("No result")

    except ValueError:
        # Print error message if response is not a valid JSON
        print("Not a valid JSON")
