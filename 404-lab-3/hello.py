#!/usr/bin/env python3

import os 
import json

# env as plain text
'''
print("Content-Type : text/plain")
print()
print(os.environ)
'''
# env as json
'''
print("Content-Type : application/json")
print()
print(json.dumps(dict(os.environ),indent=2))
'''
# query parameter in html

print("Content-Type : text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

