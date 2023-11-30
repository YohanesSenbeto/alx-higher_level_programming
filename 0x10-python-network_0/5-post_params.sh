#!/bin/bash

# Take in the URL, send a POST request with specific variables, & display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
