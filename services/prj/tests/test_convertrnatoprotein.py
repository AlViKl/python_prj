import unittest
from app.utils.gen_functions import convert_rna_to_protein


class TestConvertRNAToProtein(unittest.TestCase):
    def test_basic_convertion_1(self):
        data = "GCUAACUAAC"
        expected = "AN."
        actual = convert_rna_to_protein(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_basic_convertion_2(self):
        data = "GUUGUAAUGGCCUACAUUA"
        expected = "VVMAYI"
        actual = convert_rna_to_protein(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_basic_convertion_3(self):
        data = "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"
        expected = "PVLDWLEEKF"
        actual = convert_rna_to_protein(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_basic_convertion_4(self):
        data = "GCUAACUAACAUCUUUGGCACUGUU"
        expected = "AN.HLWHC"
        actual = convert_rna_to_protein(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_empty(self):
        data = ""
        expected = ""
        actual = convert_rna_to_protein(data)

        self.assertTrue(actual == expected,
                        f"Input {data} should be {expected}")

    def test_none(self):
        data = None

        with self.assertRaises(TypeError):
            convert_rna_to_protein(data)


if __name__ == '__main__':
    unittest.main()
