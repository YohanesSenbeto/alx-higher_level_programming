#!/bin/bash

# Take in the URL, send a request, & display only the status code of the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
echo "$response"
