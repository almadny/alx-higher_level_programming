#!/bin/bash
# Display the body of HTTP reponse using curl command
curl -sSL -X POST -H "Content-Type: application/json" -d "@$2" "$1" --fail --json-schema schema.json
