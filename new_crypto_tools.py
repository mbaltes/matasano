import binascii
import codecs
import base64
import string


def decode_xor_cipher(s, key):
    s = codecs.decode(s, 'hex')
    res = []
    for c in s:
        res.append(c ^ key)
    return bytes(res)


# Set 1.3 helper function.
def score_plaintext(s):
    count = 0
    for c in s:
        if chr(c) in string.ascii_letters:
            count += 1
    return float(count) / len(s)


# Set 1.3
def find_xor_cipher_key(s):
    s = codecs.decode(s, 'hex')
    ratio = []
    res = []
    for i in range(256):
        for j in s:
            res.append(j ^ i)
        # run freq analysis here
        #print(i, score_plaintext(bytes(res)))
        ratio.append(score_plaintext(bytes(res)))
        res = []
    max_value = max(ratio)
    max_index = ratio.index(max_value)
    return max_index


# Set 1.2
def xor(a, b):
    """Takes two equal-length hex buffers and returns their XOR combination."""
    assert len(a) == len(b), "Lengths must be equal."

    a = codecs.decode(a, 'hex')
    b = codecs.decode(b, 'hex')
    res = []
    for i in range(len(a)):
        res.append(a[i] ^ b[i])
    return binascii.hexlify(bytes(res))


# Set 1.1
def hex_to_64(s):
    """Returns the base64 encoded bytes of hex string s."""
    t = codecs.decode(s, 'hex')
    return base64.b64encode(t)


k = find_xor_cipher_key('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

solution = decode_xor_cipher('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', k)

print(solution)
