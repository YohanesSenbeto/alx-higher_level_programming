#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

# Store a URL from a command-line argument
url="$1"

# Send a GET request and display a response body
curl -sX GET "$url"
