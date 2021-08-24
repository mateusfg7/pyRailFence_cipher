def encode(string_to_encode):
    trails = {
        0: [],
        1: []
    }
    curr_trail = 0

    for letter in string_to_encode:
        trails[curr_trail].append(letter)
        curr_trail = 0 if curr_trail != 0 else 1

    cipher_message = ''.join(trails[0] + trails[1])

    return cipher_message.upper()

