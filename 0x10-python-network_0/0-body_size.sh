#!/bin/bash
# displays the size of the response
curl -Is "$1" | grep -w 'Content-Length' | wc -c
