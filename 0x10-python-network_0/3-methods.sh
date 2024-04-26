#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -L OPTIONS "$1"
