from data.rna_to_aminoacid_data import RNA_TO_AMINOACID
from app.db_management.data_queries import get_rna, get_aminoacid

CODON_LENGTH = 3


def convert_dna_to_rna(dna_sequence: str) -> str:
    """
        Input DNA sequence as a string convert to
        RNA sequence as a string using database
    """
    rna_sequence = ''
    for base in dna_sequence:
        rna_sequence += get_rna(base)
    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    """
    Convert RNA sequence to protein using database
    """
    protein = ""
    rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+CODON_LENGTH]
        if len(codon) == CODON_LENGTH:
            protein += get_aminoacid(codon)
    return protein


def convert_dna_to_rna_legacy(dna_sequence: str) -> str:
    """
        Input DNA sequence as a string convert to
        RNA sequence as a string
    """
    return dna_sequence.replace('T', 'U')


def convert_rna_to_protein_legacy(rna_sequence: str) -> str:
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
