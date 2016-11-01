# TODO: Comment code.

import binascii


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
    #return max(res, key=lambda x: x[0])
    top = max(res, key=lambda x: x[0])
    top = top[0]
    return [x for x in res if x[0] == top]


def detect_xor_cipher(file):
    res = []
    with open(file) as f:
        for line in f:
            line = ''.join(line.split())
            res.append(decode_xor_cipher(line))
    #return max(res, key=lambda x: x[0])
    return res


def print_top_results(d, data):
    for i in range(len(data)):
        if data[i][0][0] > d:
            for x in data[i]:
                print(x)


print_top_results(0.79, detect_xor_cipher('detect.txt'))

