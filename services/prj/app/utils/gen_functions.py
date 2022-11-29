from app.data.rna_to_aminoacid_data import RNA_TO_AMINOACID
from app.db_management.data_queries import get_rna, get_aminoacid
import numpy as np

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
    if isinstance(rna_sequence, str):
        rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+CODON_LENGTH]
        if len(codon) == CODON_LENGTH:
            protein += get_aminoacid(codon)
    return protein


def calculation_gc_content(sequence: str) -> int:
    '''
    Calculation of GC content in DNA/RNA
    '''
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return round((g_count + c_count) / len(sequence) * 100)


def generate_random_dna(sequence_size: int = 60) -> str:
    '''
    Generate random dna sequence
    '''
    dna_bases = ['A', 'C', 'G', 'T']
    test_data = str()
    for i in range(sequence_size):
        base = np.random.choice(dna_bases)
        test_data += base
    return test_data


def show_basic_functions(sequence_size: int = 60):
    '''
    Function to show basic functionality of convert_dna_to_rna
    and convert_rna_to_protein
    '''
    random_dna = generate_random_dna(sequence_size)
    random_rna = convert_dna_to_rna(random_dna)
    random_protein = convert_rna_to_protein(random_rna)
    print(f"Random DNA - {random_dna} to RNA - {random_rna}")
    print(f"Random RNA - {random_rna} to Protein - {random_protein}")


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
