#!/bin/python

import sys

arguments = sys.argv

if "-m" in arguments:
    message_index = arguments.index("-m") + 1
    message = arguments[message_index]
else:
    print("Pass the message to be encrypted using the option '-m'.")
    exit()

trail_1 = []
trail_2 = []
trail_switch = 1

for letter in message:
    if trail_switch == 1:
        trail_1.append(letter)
        trail_switch = 2
    else:
        trail_2.append(letter)
        trail_switch = 1
