#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()

print (type(html))
