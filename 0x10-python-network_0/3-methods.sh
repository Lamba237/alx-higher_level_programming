#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1" | grep -i 'Allow:' | cut -f2 -d' '
