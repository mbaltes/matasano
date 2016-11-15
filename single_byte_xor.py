import binascii
import base64

cipher_text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def score_plaintext(s):
    count = 0
    for i in s:
        if 'a'<=i<='z' or 'A'<=i<='Z':
            count += 1
    return float(count) / len(s)


def decode_xor_cipher(s):
    res = []
    for i in range(256):
        temp = []
        for j in binascii.unhexlify(s):
            temp.append(chr(ord(j) ^ i))
        res.append([score_plaintext(temp), ''.join(temp)])
    #return res
    return max(res, key=lambda x: x[0])


def encode_xor_cipher(key, text):
    res = ''
    temp = []
    for j in text:
        temp.append(chr(ord(j) ^ ord(key)))
    res = ''.join(temp)
    return binascii.hexlify(res)


def encode_repeating_key_xor(file, key):
    """Encrypts a file with repeating-key xor with the given key. """
    temp = []
    # ret = []
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
            # ret.append(binascii.hexlify(res))
            print(binascii.hexlify(res))
            res = ''
            # temp = []
            del temp[:]
        # return ret


# def repeating_key_decode(l):
#     for x in l:
#         print(decode_xor_cipher(x))


# encode_repeating_key_xor('secret.txt', 'Password')

a = decode_xor_cipher(cipher_text)
print a[1]

#print base64.b64decode(cipher_text)
#print binascii.unhexlify(cipher_text)