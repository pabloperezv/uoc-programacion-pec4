import unittest
from embassaments.load_data import load_dataset
from embassaments.cleaning import rename_columns, clean_station_names, filter_la_baells

class TestCleaning(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = "data/Quantitat_d_aigua_als_embassaments_de_les_Conques_Internes_de_Catalunya_20250607.csv"
        cls.raw_df = load_dataset(path)

    def test_rename_columns(self):
        df = rename_columns(self.raw_df)
        self.assertIn('dia', df.columns)
        self.assertIn('estacio', df.columns)

    def test_clean_station_names(self):
        df = rename_columns(self.raw_df)
        df = clean_station_names(df)
        self.assertFalse(df['estacio'].str.contains("Embassament de").any())
        self.assertFalse(df['estacio'].str.contains(r'\(.*\)', regex=True).any())

    def test_filter_la_baells(self):
        df = rename_columns(self.raw_df)
        df = clean_station_names(df)
        baells_df = filter_la_baells(df)
        self.assertGreater(len(baells_df), 0)
        self.assertTrue((baells_df['estacio'] == 'la Baells').all())

if __name__ == '__main__':
    unittest.main(verbosity=2)
