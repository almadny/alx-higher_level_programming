#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(response.content.decode('utf-8'))))
    print("\t- content: {}".format(response.content.decode('utf-8')))