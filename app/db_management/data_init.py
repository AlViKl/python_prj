from app.db_management.data_model import RNA, DNA, Codon, Aminoacid
from app.db_management.data_configuration import Base, Engine, Session
from data.rna_to_aminoacid_data import AMINOACID_TO_RNA


Base.metadata.create_all(Engine)


rna = [
    RNA(nucleocid='A'),
    RNA(nucleocid='C'),
    RNA(nucleocid='G'),
    RNA(nucleocid='U'),
]

dna = [
    DNA(nucleocid="A", rna_base=rna[0]),
    DNA(nucleocid="C", rna_base=rna[1]),
    DNA(nucleocid="G", rna_base=rna[2]),
    DNA(nucleocid="T", rna_base=rna[3]),
]


codons_data = list()

for aminoacid, codons in AMINOACID_TO_RNA.items():
    aminoacid = Aminoacid(aminoacid=aminoacid)
    for codon in codons:
        codons_data.append(Codon(codon=codon, aminoacid=aminoacid))


def fill_tables():
    with Session() as session:
        session.add_all(dna)
        session.commit()
        session.add_all(codons_data)
        session.commit()
