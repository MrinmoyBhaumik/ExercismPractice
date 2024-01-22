def to_rna(dna_strand):
    rna = ""
    for letter in dna_strand:
        if letter == "A":
            rna += "U"
        if letter == "G":
            rna += "C"
        if letter == "C":
            rna += "G"
        if letter == "T":
            rna += "A"
    return rna
