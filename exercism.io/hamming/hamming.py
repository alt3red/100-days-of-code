def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The 2 strands are of different length')
    hamming = 0
    for n in range(len(strand_a)):
        if strand_a[n] != strand_b[n]:
            hamming += 1
    return hamming
