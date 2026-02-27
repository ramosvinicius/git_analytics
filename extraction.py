import pandas as pd
from datetime import datetime


def load_data():
    df = pd.read_excel("data/raw/bikes.xlsx")

    df = df.reset_index().rename(columns={'index': 'id'})
    df['selling_price'] = pd.to_numeric(df['selling_price'], errors='coerce')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['km_driven'] = pd.to_numeric(df['km_driven'], errors='coerce')
    df['ex_showroom_price'] = pd.to_numeric(df['ex_showroom_price'], errors='coerce')

    df['age'] = datetime.now().year - df['year']

    # Remove colunas completamente vazias
    df = df.dropna(axis=1, how='all')

    return df