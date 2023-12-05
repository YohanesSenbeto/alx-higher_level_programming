#!/bin/bash

# Send a POST request to the server and capture the response with a maximum timeout of 10 seconds
response=$(timeout 10 curl -s -X POST "http://0.0.0.0:5000/catch_me" -d "user_id=98" -L -H "Origin: HolbertonSchool")

# Check if the response contains the message "You got me!"
if [[ $response == *"You got me!"* ]]; then
  echo "You got me!"
else
  echo "No response message found."
fi
