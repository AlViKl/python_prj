RNA_TO_AMINOACID = {
                "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F",
                "CUC": "L", "AUC": "I", "GUC": "V", "CGG": "R", "AGG": "R",
                "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "CGC": "R",
                "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "AAU": "N",
                "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "ACA": "T",
                "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "AAA": "K",
                "UCA": "S", "CCA": "P", "GCA": "A", "AGA": "R", "GGA": "G",
                "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "GAA": "E",
                "UAU": "Y", "CAU": "H", "GAU": "D", "AGC": "S", "GGC": "G",
                "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "GAG": "E",
                "CAA": "Q", "UGG": "W", "GGG": "G", "CGA": "R", "AAG": "K",
                "CAG": "Q", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                "UGC": "C", "UGA": ".", "UAA": ".", "UAG": "."
                }

AMINOACID_TO_RNA = {
        'F': ['UUU', 'UUC'],
        'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
        'Y': ['UAU', 'UAC'],
        '.': ['UAA', 'UAG', 'UGA'],
        'C': ['UGU', 'UGC'],
        'W': ['UGG'],
        'P': ['CCU', 'CCC', 'CCA', 'CCG'],
        'H': ['CAU', 'CAC'],
        'Q': ['CAA', 'CAG'],
        'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'I': ['AUU', 'AUC', 'AUA'],
        'M': ['AUG'],
        'T': ['ACU', 'ACC', 'ACA', 'ACG'],
        'N': ['AAU', 'AAC'],
        'K': ['AAA', 'AAG'],
        'V': ['GUU', 'GUC', 'GUA', 'GUG'],
        'A': ['GCU', 'GCC', 'GCA', 'GCG'],
        'D': ['GAU', 'GAC'],
        'E': ['GAA', 'GAG'],
        'G': ['GGU', 'GGC', 'GGA', 'GGG']
}
