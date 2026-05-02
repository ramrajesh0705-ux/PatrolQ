import pandas as pd

def load_data(path):
    """Load Chicago crime data from CSV"""
    print(f"Loading crimes data")
    df = pd.read_csv("data/raw/crimes.csv")
    return df