#!/bin/bash
# Display the body of HTTP reponse using curl command
curl -sSL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
