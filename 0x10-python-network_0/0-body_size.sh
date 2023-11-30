#!/bin/bash

# Usage message if no argument provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the size of the response body using curl and display in bytes
curl -s "$1" | wc -c
