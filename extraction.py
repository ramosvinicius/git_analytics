import pandas as pd
from datetime import datetime

def load_data():
    df = pd.read_csv("data/raw/bike.csv")

    df = df.reset_index().rename(columns={'index': 'id'})
    df['selling_price'] = df['selling_price'].astype(float)
    df['age'] = datetime.now().year - df['year']

    return df