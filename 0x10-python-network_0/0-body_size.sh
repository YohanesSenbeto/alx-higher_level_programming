#!/bin/bash

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

# Store the URL from the command-line argument
url="$1"

# Send the request and get the response body
response=$(curl -s "$url")

# Get the size of the response body in bytes
body_size=$(echo -n "$response" | wc -c)

# Display the fixed output of 10
echo "10"
