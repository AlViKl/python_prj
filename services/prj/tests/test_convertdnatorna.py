import unittest
from app.utils.gen_functions import convert_dna_to_rna


class TestConvertDNAToRNA(unittest.TestCase):
    def test_basic_convertion_1(self):
        data = "ATTTGGCTACTAACAATCTA"
        expected = "AUUUGGCUACUAACAAUCUA"
        actual = convert_dna_to_rna(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_basic_convertion_2(self):
        data = "GTTGTAATGGCCTACATTA"
        expected = "GUUGUAAUGGCCUACAUUA"
        actual = convert_dna_to_rna(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_basic_convertion_3(self):
        data = "CAGGTGGTGTTGTTCAGTT"
        expected = "CAGGUGGUGUUGUUCAGUU"
        actual = convert_dna_to_rna(data)

        self.assertTrue(actual == expected,
                        f"Input {data}, should be {expected}")

    def test_basic_convertion_4(self):
        data = "GCTAACTAAC"
        expected = "GCUAACUAAC"
        actual = convert_dna_to_rna(data)

        self.assertTrue(actual == expected,
                        f"Input {data}, should be {expected}")

    def test_empty(self):
        data = ""
        expected = ""
        actual = convert_dna_to_rna(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_none(self):
        data = None

        with self.assertRaises(TypeError):
            convert_dna_to_rna(data)


if __name__ == '__main__':
    unittest.main()
