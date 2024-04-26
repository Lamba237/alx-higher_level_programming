#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -x OPTIONS -I "$1" | grep -i "^allow:" | tr -d '\r'
