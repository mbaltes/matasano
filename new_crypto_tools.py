import binascii
import codecs
import base64
import string


# Set 1.4
def detect_xor_cipher(file):
    res = []
    score = 0
    max_entry = 0
    with open(file) as f:
        for line in f:
            key = find_xor_cipher_key(line.strip())
            plaintext = decode_xor_cipher(line.strip(), key)
            #print(count, plaintext)
            res.append(plaintext)
    for i, entry in enumerate(res):
        #j = score_plaintext(entry)
        j = byte_list_to_words(entry)
        if j > score:
            score = j
            max_entry = i
    return max_entry, res[max_entry]

def file_to_str(f):
    with open(f) as f:
        cipher = f.read()
    return cipher


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
    for i in range(128): # 256 is whole ascii table, 128 is mostly a-z, A-Z
        for j in s:
            res.append(j ^ i)
        # run freq analysis here
        #print(i, score_plaintext(bytes(res)))
        #ratio.append(score_plaintext(bytes(res)))
        ratio.append(byte_list_to_words(bytes(res)))
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


def get_word_list():
    s = set()
    with open('english-words-10k.txt') as file:
        for f in file:
            s.add(f.strip())
    return s


def byte_list_to_words(l):
    words = ENGLISH_WORDS
    count = 0
    temp = ''
    for c in l:
        if chr(c) in string.ascii_letters:
            temp += chr(c).lower()
        else:
            if temp in words and len(temp) > 1:
                #print(temp)
                count += 1
            temp = ''
    return count


# Set 1 challenge 5
def encode_repeating_key_xor(file, key):
    f = file_to_str(file)
    res, out = [], []
    for line in f:
        for c in line:
            res.append(ord(c))
    i = 0
    for n in bytes(res):
        if i < len(key):
            out.append(n ^ ord(key[i]))
            i += 1
        else:
            i = 0
            out.append(n ^ ord(key[i]))
            i += 1
    return binascii.hexlify(bytes(out))


ENGLISH_WORDS = get_word_list()
