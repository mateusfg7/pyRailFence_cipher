#!/bin/python

import sys
from encode import encode
from decode import decode

arguments = sys.argv

if "-h" in arguments:
    print("""
A Python script to encode messages using the Rail Fence algorithm.
By Mateus Felipe Gonçalves <mateusfg7@protonmail.com>

Usage: rail-fence.py [options] -m [message]

options:
    e   encode a message.
    d   decode a message.
params:                                                                              
    -h   help menu.                                                                    
    -m   message to be ciphered. e.g.: -m "message"
    """)
    exit()

if "-m" in arguments:
    message_index = arguments.index("-m") + 1
    message = arguments[message_index]
else:
    print("Pass the message to be encrypted using the option '-m'.")
    exit()

if "e" in arguments:
    print(f"""
    Message:
    {message.lower()}

    Encoded Message:
    {encode(message)}
    """)
elif "d" in arguments:
    print(f"""
    Message:
    {message.upper()}
    
    Decoded Message:
    {decode(message)}
    """)
