#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -x OPTIONS "$1"
