#!/bin/bash
## Take the URL as an argument, send a GET request with a custom header, & display the body of the response

curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
