#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL argument in a variable
url="$1"

# Send a DELETE request to the URL and store the response in a variable
response=$(curl -s -X DELETE "$url")

# Check if the request was successful (HTTP status code 2xx)
if [[ $? -eq 0 && $response != *"\"success\":false"* ]]; then
  echo "Request successful"
  echo "$response"
else
  echo "Request failed"
fi
