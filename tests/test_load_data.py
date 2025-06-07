import unittest
from embassaments.load_data import load_dataset

class TestLoadData(unittest.TestCase):
    def setUp(self):
        self.path = "data/Quantitat_d_aigua_als_embassaments_de_les_Conques_Internes_de_Catalunya_20250607.csv"
        self.df = load_dataset(self.path)

    def test_load_dataset_not_none(self):
        self.assertIsNotNone(self.df)

    def test_load_dataset_not_empty(self):
        self.assertFalse(self.df.empty)

    def test_load_dataset_has_columns(self):
        self.assertGreater(len(self.df.columns), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
