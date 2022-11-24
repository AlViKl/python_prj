from app.utils.gen_functions import convert_rna_to_protein, convert_dna_to_rna
from app.db_management.data_init import fill_tables
from app.db_management.data_queries import get_rna, get_aminoacid

def main():
    fill_tables()
    # to move to tests
    print(convert_dna_to_rna("GCTAACTAACATCTTTGGCACTGTT"))
    print(convert_rna_to_protein("CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"))
    print(convert_rna_to_protein("CAGGUGGUGUUGUUCAGUU"))


if __name__ == "__main__":
    main()
