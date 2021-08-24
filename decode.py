from math import ceil
import sys

arg = sys.argv[1]

def decode(string_to_decode):

    LENGHT = len(string_to_decode)

    middle_string = ceil(LENGHT / 2)
    
    trails = [
        string_to_decode[0:middle_string],
        string_to_decode[middle_string:LENGHT]
    ]

    message_letter_list = []

    for index in range(0, middle_string):
        message_letter_list.append(trails[0][index])
        
        if not index >= len(trails[1]):
            message_letter_list.append(trails[1][index])

    message = ''.join(message_letter_list)

    return message.lower()

if __name__ == "__main__":
    print(decode(arg))
