# These functions are deprecated. Written in python 2 and incomplete.
# See the rewritten functions in new_crypto_tools.


# TODO: Find correct order of decryption sequence. Make sure decode single
# xor is solid. Work my way up.
#

import collections
import base64


def break_repeated_xor(file):
    res = []
    words = []
    s = file_to_str(file)
    #print s
    keys = guess_keysize(s)  # keys = [(1, 5), (2, 2), (2, 3)]
    print keys
    # print keys
    # for e in keys: 
    #     if e[1] == 29:
    #         b = block(s, e[1])  # ['str of len 5', etc]
    #         l = transpose(b, e[1])  # ['transposed str of len 5', etc]
    #         # solve each block as if singlecharxor
    #         for x in l:
    #             #res.append(decode_xor_cipher(binascii.hexlify(x)))
    #             res.append(decode_xor_cipher(x.encode('hex')))
    #             #res.append(decode_xor_cipher(x))
    #             #break
    #         #print res
    #         top = ''
    #         for d in res:
    #             for j, k in enumerate(d):
    #                 print collections.Counter(k[1]).most_common(1)[0]
    #                 break
    #             # print collections.Counter(k[j][]).most_common(1)[0]
    #             # top += temp[0]
    #             # words.append(''.join(top))
    #             # break
    #             # print collections.Counter(d).most_common(1)[0]
    #             # print collections.Counter(d).most_common(1)
    #             # temp = temp[0]
    #             # print d.replace('\n', '')
    #             # m += temp
    #             # print d
    #             # break
    #             # m += d
    #             #break
    #             break
    #         print top
    #         res = []
    # #return res
    # #return top

def transpose(list, size):
    """
    Transposes the blocks by making a block that is the first byte of every 
    block, and a block that is the second byte of every block, etc.
    Returns a list of transposed blocks.

    """
    res = [[] for x in range(size)]
    for outer, elem in enumerate(list):
        for inner, x in enumerate(elem):
            res[inner].append(x)

    for x, y in enumerate(res):
        res[x] = ''.join(y)
    return res


def block(str, size):
    """
    Blocks ciphertext into blocks of keysize length. Returns list of these 
    blocks.

    """
    res = []
    count = 0
    for x in str:
        if count + size > len(str): break
        res.append(str[count:count+size])
        count += size
    return res


def file_to_str(f):
    with open(f) as f:
        cipher = f.read()
    return cipher.decode('base64')


def guess_keysize(s):
    """
    Guesses size of the encryption key from incoming string. Returns list of 
    results in the form [hamming dist, keysize]. Only returns the 3 smallest 
    hamming dist keysizes. 

    """
    keysize = []
    start, end = 2, 40
    for n in range(start, end):
        r = n + n
        if r > len(s): break
        temp = hamming_dist(s[:n], s[n:r]) / float(n)
        keysize.append([temp, n])
    keysize.sort()
    return keysize


def to_bin(s):
    """Returns binary representation of s buffered to 10-digits."""
    temp = [bin(ord(ch))[2:].zfill(10) for ch in s]
    return ''.join(temp)


def hamming_dist(a, b):
    """Returns the Hamming distance between two strings."""
    assert len(a) == len(b), "Strings must have same length."
    return sum(x != y for x, y in zip(to_bin(a), to_bin(b)))
    

def encode_xor_cipher(key, text):
    temp = []
    for x in text:
        temp.append(chr(ord(x) ^ ord(key)))
    res = ''.join(temp)
    return res.encode('hex')


# Set 1 challenge 5
def encode_repeating_key_xor(file, key):
    """Encrypts a file with repeating-key xor with the given key. """
    encoded = []
    temp = []
    i = 0
    with open(file) as file:
        for line in file:
            for n in line:
                if i < len(key):
                    temp.append(chr(ord(n) ^ ord(key[i])))
                    i += 1
                else:
                    i = 0
                    temp.append(chr(ord(n) ^ ord(key[i])))
                    i += 1
            res = ''.join(temp)
            encoded.append(res.encode('hex'))
            res = ''
            del temp[:]
    return ''.join(encoded)


# Set 1 challenge 4
def detect_xor_cipher(file):
    res = []
    with open(file) as f:
        for line in f:
            res.append(decode_xor_cipher(line.strip()))
    #return max(res, key=lambda x: x[0])
    return res

# Set 1 challenge 4 helper function
def print_top_results(d, data):
    for i in range(len(data)):
        if data[i][0][0] > d:
            for x in data[i]:
                print(x)


# Set 1 challenge 3 helper function
def score_plaintext(s):
    """Returns ratio of a-z and A-Z characters in a string."""
    count = 0
    for i in s:
        if 'a'<=i<='z' or 'A'<=i<='Z':
            count += 1
    return float(count) / len(s)


# Set 1 challenge 3
def decode_xor_cipher(s):
    s = s.decode("hex")
    res = []
    for i in range(256):
        temp = []
        for j in s:
            temp.append(chr(ord(j) ^ i))
        res.append([score_plaintext(temp), ''.join(temp)])
    #return res
    #return max(res, key=lambda x: x[0])
    top = max(res, key=lambda x: x[0])
    top = top[0]
    return [x for x in res if x[0] == top]


# Set 1 challenge 2
def xor(a, b):
    """Takes two equal-length hex buffers and returns their XOR combination."""
    assert len(a) == len(b), "Lengths must be equal."

    a = a.decode("hex")
    b = b.decode("hex")
    res = []
    for i, x in enumerate(a):
        res.append(chr(ord(x) ^ ord(b[i])))
    ans = ''.join(res)
    return ans.encode("hex")


# Set 1 challenge 1
def hex_to_64(s):
    """Returns the hex encoded string s to a base64 encoded string."""
    t = s.decode('hex')
    return t.encode('base64').strip()
