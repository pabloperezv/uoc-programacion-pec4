''' Este modulo sirve para cargar los datos'''
import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """Carga el dataset desde un csv descargado en local."""
    df = pd.read_csv(path)
    return df
