import pandas as pd

def clean_data(df):
    """
    Robust cleaning for large, messy Chicago crime data
    """

    # 1️⃣ Drop rows without geo coordinates
    df = df.dropna(subset=["Latitude", "Longitude"]).copy()

    # 3️⃣ Parse datetime safely (mixed formats)
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')


    df['month'] = df['Date'].dt.month
    df['hour'] = df['Date'].dt.hour
    df['day_num'] = df['Date'].dt.dayofweek
    
    df[["month", "day_num", "hour"]] = df[["month", "day_num", "hour"]].astype("int8")
    df["Year"] = df.Year.astype("int16")
    
    df.drop(['ID','Case Number','Updated On'],axis=1,inplace=True)
    df = df.sample(n=500000,random_state=42)

    return df