import pandas as pd
from datetime import datetime


def load_data():
    df = pd.read_excel("data/raw/bikes.xlsx")

    df = df.reset_index().rename(columns={'index': 'id'})

    numeric_columns = ['selling_price', 'year', 'km_driven', 'ex_showroom_price']

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'year' in df.columns:
        df['age'] = datetime.now().year - df['year']

    df = df.dropna(axis=1, how='all')

    return df