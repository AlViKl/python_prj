from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from app.db_management.data_configuration import Base


'''
Database schema definition
'''


class DNA(Base):
    '''
    Table for DNA
    '''
    __tablename__ = 'dna_bases'
    __tablearg__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nucleocid = Column(String(1), unique=True)
    rna_base = relationship('RNA', back_populates='dna_base')
    rna_base_id = Column(Integer, ForeignKey('rna_bases.id'))

    def __repr__(self) -> str:
        return f"{self.nucleocid, self.rna_base}"


class RNA(Base):
    '''
    Table for RNA
    '''
    __tablename__ = 'rna_bases'
    __tablearg__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nucleocid = Column(String(1), unique=True)
    dna_base = relationship('DNA', back_populates='rna_base')

    def __repr__(self) -> str:
        return f"{self.nucleocid}"


class Codon(Base):
    '''
    Table for Codon
    '''
    __tablename__ = 'triplet'
    __tablearg__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    codon = Column(String(3))
    aminoacid = relationship('Aminoacid', back_populates='codon')
    aminoacid_id = Column(Integer, ForeignKey('aminoacid.id'))

    def __str__(self) -> str:
        return f"{self.codon}"


class Aminoacid(Base):
    '''
    Table for Aminoacid
    '''
    __tablename__ = 'aminoacid'
    __tablearg__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    aminoacid = Column(String(1), unique=True)
    codon = relationship('Codon', back_populates='aminoacid')

    def __str__(self) -> str:
        return f"{self.aminoacid}"
