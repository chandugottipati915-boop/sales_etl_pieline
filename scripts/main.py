from extract_csv import extract_csv
from transform import transform_sales
from load import load_to_db

def run_pipeline():
    df = extract_csv("data/raw/sales.csv")
    clean_df = transform_sales(df)
    load_to_db(clean_df)

if __name__ == "__main__":
    run_pipeline()