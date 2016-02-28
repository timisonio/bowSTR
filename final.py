#!/usr/local/cs/Python-2.7.9/bin/python2
import itertools
import sys
from array import array
from collections import defaultdict, Counter

possible_str_lengths = (3, 4, 5)
minimum_repeats_to_be_str = 3

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
        ref = ''.join([line.strip() for line in ref_file])

    three_mers = defaultdict(list)
    four_mers = defaultdict(list)
    five_mers = defaultdict(list)
    for i in range(len(ref) - 5):
        three_mers[ref[i:i+3]].append(i)
        four_mers[ref[i:i+4]].append(i)
        five_mers[ref[i:i+5]].append(i)

    strs = defaultdict(list)
    for key in three_mers:
        repeat_length = 1
        num_instances = len(three_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and three_mers[key][i] - three_mers[key][i+j] == -j*3:
                j += 1
            if j >= 3:
                strs[key*j] = three_mers[key][i]

    for key in four_mers:
        repeat_length = 1
        num_instances = len(four_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and four_mers[key][i] - four_mers[key][i+j] == -j*4:
                j += 1
            if j >= 3:
                strs[key*j] = four_mers[key][i]

    for key in five_mers:
        repeat_length = 1
        num_instances = len(five_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and five_mers[key][i] - five_mers[key][i+j] == -j*5:
                j += 1
            if j >= 3:
                strs[key*j] = five_mers[key][i]

    for key in strs:
        print key, strs[key]
    
    # k_kmers = {}
    # for k in range(3, 6):
    #     k_kmers[k] = kmers(k)
    seq = 'acaacg'
    # print bwt(''.join(ref))     
            
