#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -L -X PUT -d "user_id=98" -H "origin: school" 0.0.0.0:5000/catch_me
