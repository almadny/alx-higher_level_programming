#!/bin/bash
# Display the body of HTTP reponse using curl command
curl -sSL -X POST -H "Content-Type: application/json" -d @my_json_0 "$1"
