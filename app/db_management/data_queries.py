from app.db_management.data_model import DNA, RNA, Codon, Aminoacid
from app.db_management.data_configuration import Session


def get_rna(nucleocid: str) -> str:
    with Session() as session:
        rna = session.query(RNA).join(DNA).\
                filter(DNA.nucleocid == nucleocid).one()
        return str(rna)


def get_aminoacid(codon: str) -> str:
    with Session() as session:
        aminoacid = session.query(Aminoacid).join(Codon).\
                filter(Codon.codon == codon).one()
        return str(aminoacid)
