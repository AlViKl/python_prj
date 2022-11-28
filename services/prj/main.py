from app.utils.gen_functions import convert_rna_to_protein, convert_dna_to_rna
from app.utils.gc_plot import generate_plot_with_data
from app.db_management.data_init import fill_tables
from app.db_management.data_configuration import db_drop, db_create
from app.db_management.data_queries import get_rna, get_aminoacid

def main():
    db_drop()
    db_create()
    fill_tables()
    # to move to tests
    print(convert_dna_to_rna("GCTAACTAACATCTTTGGCACTGTT"))
    print(convert_rna_to_protein("CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"))
    print(convert_rna_to_protein("CAGGUGGUGUUGUUCAGUU"))
    # function to test plot with some test data
    generate_plot_with_data()


if __name__ == "__main__":
    main()
