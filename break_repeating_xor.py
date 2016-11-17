import binascii
import base64
import collections


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
    return res
    #return max(res, key=lambda x: x[0])


def break_repeated_xor(file):
    res = []
    words = []
    s = file_to_str(file)
    #print s
    keys = guess_keysize(s)  # keys = [(1, 5), (2, 2), (2, 3)]
    #print keys
    for e in keys: 
        #if e[1] == 29:
        print 'Key Length: %s' % e[1]
        m = ''
        b = block(s, e[1])  # ['str of len 5', etc]
        l = transpose(b, e[1])  # ['transposed str of len 5', etc]
        print l
        # solve each block as if singlecharxor
        for x in l:
            res.append(decode_xor_cipher(binascii.hexlify(x)))
            #res.append(decode_xor_cipher(x))
            #break
        #print res
        top = ''
        for i, d in enumerate(res):
            temp = collections.Counter(d[i][1]).most_common(1)[0]
            top += temp[0]
            #words.append(''.join(top))
            #break
            #print collections.Counter(d).most_common(1)[0]
            #print collections.Counter(d).most_common(1)
            #temp = temp[0]
            # print d.replace('\n', '')
            # m += temp
            #print c, d
            #m += d
        print top
        res = []
    #return res
    #return top


def transpose(list, size):
    """Transposes the blocks by making a block that is the first byte of 
       every block, and a block that is the second byte of every block, etc.
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
            l.append(line)
            #l.append(''.join(line.split()))
    res = ''.join(l)
    #return res
    #return base64.b64decode(res)
    #res = binascii.unhexlify(res)
    res = res.decode("base64")
    #res = res.encode("hex")
    return res


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
    #return ret[:3]
    return ret


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
# print len(m)
#print m


# a = hamming_dist('hello world', 'hello world')
# print(a)

# g = guess_keysize('this is a test', 'wokka wokka!!!')
# g = guess_keysize2('abcweurpoweiurqweiabcqoiweurpweabc')
# print(g)

# f = file_to_str('6.txt')
# print(f)
# print(type(f))

# g = guess_keysize2(file_to_str('6.txt'))
# print(g)

# r = block(file_to_str('6.txt'), 5)
# print r

# test = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i']]
# l = transpose(test, 3)
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