#!/usr/bin/bash
# displays the size of the response
curl -s "$2""$3" | wc -c
