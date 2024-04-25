#!/usr/bin/bash
# displays the size of the response
curl -sI $1 | grep "content-Length" | cut -d " " -f2
