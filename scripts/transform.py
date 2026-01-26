import pandas as pd

def transform_sales(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["total_amount"] = df["quantity"] * df["price"]

    # basic validation
    df = df[df["quantity"] > 0]
    df = df.drop_duplicates()

    print("Data transformed")
    return df