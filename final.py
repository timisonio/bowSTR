#!/usr/local/cs/Python-2.7.9/bin/python2
import itertools
import sys
from array import array
from collections import defaultdict, Counter

possible_str_lengths = (2, 3, 4, 5)
minimum_repeats_to_be_str = (0, 0, 5, 5, 4, 3)#_3mer = 5
minimum_repeats_to_be_str_3mer = 5
minimum_repeats_to_be_str_4mer = 4
minimum_repeats_to_be_str_5mer = 3

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

def get_kmer_loci(reference):
    kmer_loci = [defaultdict(list) for i in range(0, 6)]

    for i in range(len(reference)-5):
        kmer_loci[2][reference[i:i+2]].append(i)
        kmer_loci[3][reference[i:i+3]].append(i)
        kmer_loci[4][reference[i:i+4]].append(i)
        kmer_loci[5][reference[i:i+5]].append(i)

    return kmer_loci
    

if __name__ == "__main__":
    chr = sys.argv[1]
    ref = []
    with open('./{}/ref_{}.txt'.format(chr, chr), 'r') as ref_file:
        ref_file.readline()  # throw away header
        ref = ''.join([line.strip() for line in ref_file])

    three_mers = defaultdict(list)
    four_mers = defaultdict(list)
    five_mers = defaultdict(list)
    two_mers = defaultdict(list)
    for i in range(len(ref) - 5):
        two_mers[ref[i:i+2]].append(i)
        three_mers[ref[i:i+3]].append(i)
        four_mers[ref[i:i+4]].append(i)
        five_mers[ref[i:i+5]].append(i)

    kmer_loci = get_kmer_loci(ref)

    loci_covered = [False for position in range(len(ref))]
    strs = {}

    # for kmer_length in range(5, 1, -1): # it's best if I go backwards
    #     for key in kmer_loci[kmer_length]:
    #         repeat_length = 1
    #         num_instances = len(kmer_loci[kmer_length][key])
    #         for i in range(num_instances):
    #             j = 1
    #             while i+j < num_instances and kmer_loci[kmer_length][key][i] - kmer_loci[kmer_length][key][i+j] == -j*kmer_length:
    #                 j += 1
    #             if j >= minimum_repeats_to_be_str[kmer_length]:
    #                 already_found = False
    #                 for locus in range(i, i+j):
    #                     if loci_covered[locus] is True:
    #                         already_found = True
    #                         break
    #                 if already_found is False:
    #                     for locus in range(i, i+j):
    #                         loci_covered[locus] = True
    #                     strs[key*j] = kmer_loci[kmer_length][key][i]
    
    for key in five_mers:
        repeat_length = 1
        num_instances = len(five_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and five_mers[key][i] - five_mers[key][i+j] == -j*5:
                j += 1
            if j > 22: print("Thanks Doga", j, file=sys.stderr)
            if j >= minimum_repeats_to_be_str_5mer:
                already_found = False
                for locus in range(i, i+j):
                    if loci_covered[locus] is True:
                        already_found = True
                        break
                if already_found is False:
                    for locus in range(i, i+j):
                        loci_covered[locus] = True
                    strs[key*j] = five_mers[key][i]



    for key in four_mers:
        repeat_length = 1
        num_instances = len(four_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and four_mers[key][i] - four_mers[key][i+j] == -j*4:
                j += 1
            if j > 22: print("Thanks Doga", j, file=sys.stderr)
            if j >= minimum_repeats_to_be_str_4mer:
                already_found = False
                for locus in range(i, i+j):
                    if loci_covered[locus] is True:
                        already_found = True
                        break
                if already_found is False:
                    for locus in range(i, i+j):
                        loci_covered[locus] = True
                    strs[key*j] = four_mers[key][i]

    for key in three_mers:
        repeat_length = 1
        num_instances = len(three_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and three_mers[key][i] - three_mers[key][i+j] == -j*3:
                j += 1
            if j > 22: print("Thanks Doga", j, file=sys.stderr)
            if j >= minimum_repeats_to_be_str_3mer:
                already_found = False
                for locus in range(i, i+j):
                    if loci_covered[locus] is True:
                        already_found = True
                        break
                if already_found is False:
                    for locus in range(i, i+j):
                        loci_covered[locus] = True
                    strs[key*j] = three_mers[key][i]
                    
    for key in two_mers:
        repeat_length = 1
        num_instances = len(two_mers[key])
        for i in range(num_instances):
            j = 1
            while i+j < num_instances and two_mers[key][i] - two_mers[key][i+j] == -j*2:
                j += 1
            if j > 22: print("Thanks Doga", j, file=sys.stderr)
            if j >= minimum_repeats_to_be_str_3mer:
                already_found = False
                for locus in range(i, i+j):
                    if loci_covered[locus] is True:
                        already_found = True
                        break
                if already_found is False:
                    for locus in range(i, i+j):
                        loci_covered[locus] = True
                    strs[key*j] = two_mers[key][i]

#    print(loci_covered.count(True), file=sys.stderr)
    # keys_to_delete = []
    # for key in strs:
    #     for key_2 in strs:
    #         if strs[key] in range(strs[key_2], strs[key_2]+ len(key_2)):
    #             keys_to_delete.append(key_2)

    # for key in keys_to_delete:
    #     if key in strs:
    #         del strs[key]
    print('>' + chr)
    print(">STR")
    for key in strs.keys():
        print(key + ',' + str(strs[key]))
    print('\n'.join([">CNV", ">INV", ">INS", ">DEL", ">SNP", ">ALU"]))
    # k_kmers = {}
    # for k in range(3, 6):
    #     k_kmers[k] = kmers(k)
    seq = 'acaacg'
    # print bwt(''.join(ref))     
            
