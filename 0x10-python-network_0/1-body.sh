#!/bin/bash
#send a GET request to the URL

response=$(curl -s -o /dev/null -w "%{http_code}" $1)

if [ "$response" -eq 200 ]; then
	body=$(curl -s $1)
	echo "$body"
fi
