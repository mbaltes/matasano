import binascii
import base64


def decode_xor_cipher(s):
    res = []
    for i in range(256):
        temp = []
        for j in binascii.unhexlify(s):
            temp.append(chr(ord(j) ^ i))
        res.append([score_plaintext(temp), ''.join(temp)])
    #return res
    return max(res, key=lambda x: x[0])


def break_repeated_xor(file):
    res = []
    s = file_to_str(file)
    keys = guess_keysize(s)
    for e in keys:
        b = block(s, e[1])
        print b
        #l = transpose(b)
        #print l
        break
    #     # solve each block as if singlecharxor
    #     for x in l:
    #         print x
    #         # res.append(temp[1])
    # return res


def transpose(l):
    """Transposes the blocks by making a block that is the first byte of 
       every block, and a block that is the second byte of every block, etc.
       Returns a list of transposed blocks.
    """
    res = [[] for x in range(len(l))]
    for outer, elem in enumerate(l):
        for inner, x in enumerate(elem):
            res[inner].append(x)
    return res


def block(str, size):
    """Blocks ciphertext into blocks of keysize length. Returns list of 
       these blocks.
    """
    res = []
    count = 0
    for x in str:
        if count + size > len(str): break
        res.append(str[count:count+size])
        count += size
    return res


def file_to_str(file):
    l = []
    with open(file) as file:
        for line in file:
            #l.append(line)
            #l.append(''.join(line.split()))
            line = ''.join(line.split())
            l.append(line)
    res = ''.join(l)
    #return res
    #return base64.b64decode(res)
    #res = binascii.unhexlify(res)
    return res.decode("base64")


def guess_keysize(s):
    """Guesses size of the encryption key from incoming string.
       Returns list of tuples in the form (hamming dist, keysize).
       Only returns the 3 smallest hamming dist keysizes. 
    """
    keysize = set()
    start, end = 2, 40
    for n in range(start, end):
        r = n + n
        if r > len(s): break
        temp = hamming_dist(s[:n], s[n:r]) / n
        keysize.add((temp, n))
    ret = list(keysize)
    ret.sort()
    return ret[:3]


def hamming_dist(a, b):
    """Hamming distance is the number of differing bits in the strings."""
    assert len(a) == len(b), "Strings must have same length."
    c = bin(int(binascii.hexlify(a), 16))
    d = bin(int(binascii.hexlify(b), 16))
    e = int(c, 2) ^ int(d, 2)
    count = 0
    for x in bin(e):
        if x == '1': count += 1
    return(count)


break_repeated_xor('6.txt')


# a = hamming_dist('hello world', 'hello world')
# print(a)

# g = guess_keysize('this is a test', 'wokka wokka!!!')
# g = guess_keysize2('abcweurpoweiurqweiabcqoiweurpweabc')
# print(g)

# f = file_to_str('6.txt')
# print(f)
#print(type(f))

# g = guess_keysize2(file_to_str('6.txt'))
# print(g)

# r = block(file_to_str('6.txt'), 5)
# print r

# test = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# l = transpose(test)
# print l


# def guess_keysize(a, b):
#     keysize = []
#     start, end = 2, 40
#     for n in range(start, end):
#         if n > len(a) / 2: break
#         temp = hamming_dist(a[:n], b[n:]) / n
#         keysize.append(temp)
#     keysize.sort()
#     return keysize[:3]