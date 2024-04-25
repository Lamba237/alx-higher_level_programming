#!/bin/bash
#send a GET request to the URL

response=$(curl -L -s -X HEAD -w "%{http_code}" "$1")

if [ "$response" -eq 200 ]; then
	curl -Ls "$1"
fi
