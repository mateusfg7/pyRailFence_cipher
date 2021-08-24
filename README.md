# pyRailFence Cipher
A Python script to encode messages using the Rail Fence algorithm.

This script was made to study the many ways to encode a message described in [_The Code Book_](https://en.wikipedia.org/wiki/The_Code_Book), of [Simon Singh](https://en.wikipedia.org/wiki/Simon_Singh).

## Usage


main.py [options] **-m [_message_]**

options:
- **e** _encode a message_
- **d** _decode a message_

params:
- `-h` _help menu_
- `-m` _message to be ciphered. e.g.: `-m "message"`_


e.g.:
```bash
python main.py e -m "mateus"
```
```bash
  Message:
  mateus
  
  Encoded Message:
  MTUAES

```

## References

- [Rail Fence Cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher) (Wikipedia article)
- [Rail Fence Cipher](https://crypto.interactive-maths.com/rail-fence-cipher.html) (Online Encode/Decoder)
- [Symmetric Key Cryptography: The Rail Fence Cipher](https://www.youtube.com/watch?v=wKjRwJTXQH4) (Youtube video)
