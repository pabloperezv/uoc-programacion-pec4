''' Este modulo sirve para la limpieza de datos'''
import re
import pandas as pd
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Renombra las columnas según el diccionario especificado."""
    rename_dict = {
        'Dia': 'dia',
        'Estació': 'estacio',
        'Nivell absolut (msnm)': 'nivell_msnm',
        'Percentatge volum embassat (%)': 'nivell_perc',
        'Volum embassat (hm3)': 'volum'
    }

    return df.rename(columns=rename_dict)

def get_unique_stations(df: pd.DataFrame) -> list:
    """Devuelve los nombres únicos de embalses (estaciones)."""
    return df['estacio'].unique().tolist()

def clean_station_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia los nombres de los pantanos eliminando 'Embassament de ' y
    el municipio entre paréntesis. Ejemplo:
    'Embassament de Darnius Boadella (Darnius)' → 'Darnius Boadella'
    """
    df['estacio'] = df['estacio'].apply(lambda x: re.sub(r'^Embassament de ', '', x))
    df['estacio'] = df['estacio'].apply(lambda x: re.sub(r'\s*\(.*?\)', '', x))
    return df

def filter_la_baells(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra y devuelve solo los registros del embalse 'La Baells'."""
    return df[df['estacio'] == 'la Baells'].copy()
