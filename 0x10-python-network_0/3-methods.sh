#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -X -I OPTIONS "$1" | grep 'Allow:' | cut -f2 -d' '
