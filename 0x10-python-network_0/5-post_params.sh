#!/bin/bash
# The Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

URL="$1"
curl -sX POST "$URL" -d "email=test@gmail.com&subject=I will always be here for PLD"

