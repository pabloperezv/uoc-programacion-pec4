import unittest
from embassaments.eda import display_head, display_columns
from embassaments.load_data import load_dataset

class TestEDA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = load_dataset("data/Quantitat_d_aigua_als_embassaments_de_les_Conques_Internes_de_Catalunya_20250607.csv")

    def test_display_head_returns_correct_rows(self):
        head = display_head(self.df, 3)
        self.assertEqual(len(head), 3)

    def test_display_columns_returns_list(self):
        cols = display_columns(self.df)
        self.assertIsInstance(cols, list)
        self.assertGreater(len(cols), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
