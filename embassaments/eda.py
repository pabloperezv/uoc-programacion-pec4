''' Este modulo sirve para el análisis exploratorio de datos'''
def display_head(df, n=5):
    """Devuelve las primeras n filas del dataframe."""
    return df.head(n)

def display_columns(df):
    """Devuelve la lista de columnas del dataframe."""
    return df.columns.tolist()

def display_info(df):
    """Muestra la información general del dataframe."""
    return df.info()
