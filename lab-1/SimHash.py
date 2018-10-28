import sys
from hashlib import md5

def simhash(text):
    sh = [0] * 128
    input_vector = text.split(' ')
    for vector in input_vector:
        hash = md5(vector.encode('utf-8')).hexdigest()
        bits = hex_to_bin(hash)

        for bit, i in zip(bits, range(len(bits))):
            sh[i] += 1 if bit == '1' else -1

    binary_list = list(map(lambda x: '1' if x >= 0 else '0', sh))
    return hex(int(''.join(binary_list), 2))

def hex_to_bin(hex_number):
    return bin(int(hex_number, 16))[2:].zfill(128)

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def get_texts_with_distance(hash, hashes, distance):
    bin_hash = hex_to_bin(hash)
    return list(filter(lambda x: hamming_distance(bin_hash, hex_to_bin(x)) <= distance, hashes))

if __name__ == '__main__':
    hashes = []
    N = int(sys.stdin.readline())

    for i in range(N):
        text = sys.stdin.readline()
        hashes.append(simhash(text.rstrip(' \n')))

    Q = int(sys.stdin.readline())

    for i in range(Q):
        query = sys.stdin.readline()
        [i, k] = list(map(int, query.split(' ')))
        hash_distances = get_texts_with_distance(hashes[i], hashes[:i] + hashes[(i + 1):], k)
        print(len(hash_distances))
