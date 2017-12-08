def to_rna(dna_strand):
    code = {
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U"
    }
    decode = ''
    for n in dna_strand:
        if n not in code:
            raise ValueError('Invalid entry!')
        decode += code[n]
    return decode
