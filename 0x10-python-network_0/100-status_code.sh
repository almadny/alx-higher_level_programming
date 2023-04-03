#!/bin/bash
# Display the body of HTTP reponse using curl command
curl -s -o /dev/null -w "%{response_code}" "$1"
