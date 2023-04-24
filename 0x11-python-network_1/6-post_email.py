#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import requests
import sys


if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    url = sys.argv[1]
    response = requests.post(url, data=data)
    print(f"{response.text}")
