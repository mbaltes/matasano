import binascii

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


print(decode_xor_cipher(cipher_text))