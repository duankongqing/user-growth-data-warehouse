import pandas as pd
from pathlib import Path

data_path = Path(__file__).parent.parent / "data"

def extract_csv(file_name):

    df = pd.read_csv(data_path / file_name)

    df["etl_time"] = pd.Timestamp.now()
    df["source_file"] = file_name

    return df

def extract_users():
    return pd.read_csv(data_path / "users.csv")

def extract_events():
    return pd.read_csv(data_path / "events.csv")

def extract_orders():
    return pd.read_csv(data_path / "orders.csv")