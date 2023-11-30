#!/bin/bash

# Take the URL as an argument, send a GET request with a custom header, & display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
