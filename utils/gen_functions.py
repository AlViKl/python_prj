from data.rna_to_aminoacid_data import RNA_TO_AMINOACID

CODON_LENGTH = 3


def convert_dna_to_rna(dna_sequence: str) -> str:
    """
        Input DNA sequence as a string covert to
        RNA sequence as a string
    """
    return dna_sequence.replace('T', 'U')


def convert_rna_to_protein(rna_sequence: str) -> str:
    """
    Convert RNA sequence to protein
    """
    protein = ""
    rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+CODON_LENGTH]
        if len(codon) == CODON_LENGTH:
            protein += RNA_TO_AMINOACID[codon]
    return protein
