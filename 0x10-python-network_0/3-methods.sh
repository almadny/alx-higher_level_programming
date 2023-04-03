#i!/bin/bash
# Display the body of HTTP reponse using curl command
curl -sSLI "$1" | sed -n 's/^Allow: //ip' 
