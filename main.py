#!/bin/python

import sys
from encode import encode

arguments = sys.argv

if "-m" in arguments:
    message_index = arguments.index("-m") + 1
    message = arguments[message_index]
else:
    print("Pass the message to be encrypted using the option '-m'.")
    exit()

print(f"\nMessage: {message}\nCipher: {encode(message)}")
