#!/usr/local/cs/Python-2.7.9/bin/python2
import itertools
import sys
from array import array

def bwt(string):
    T = array('c', string)
    T.append('$')
    
    matrix = []
    for i in range(len(T)):
        matrix.append(T[-i:] + T[:-i])
    matrix.sort()
    
    out = array('c')
    for row in matrix:
        out.append(row[len(T)-1])
    return out


def kmers(k):
    return [''.join(p) for p in itertools.product(['A', 'T', 'C', 'G'], repeat=k)]


if __name__ == "__main__":
    chr = sys.argv[1]
    ref = []
    with open('./{}/ref_{}.txt'.format(chr, chr), 'r') as ref_file:
        ref_file.readline()  # throw away header
        for line in ref_file:
            ref.append(line.strip())

    # k_kmers = {}
    # for k in range(3, 6):
    #     k_kmers[k] = kmers(k)
    seq = 'acaacg'
    print bwt(''.join(ref))
            
