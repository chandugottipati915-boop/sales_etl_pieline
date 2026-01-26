import requests
import pandas as pd

def extract_api():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data)

    # keep only useful columns
    df = df[["id", "title", "price", "category"]]
    df.rename(columns={
        "id": "product_id",
        "title": "product_name"
    }, inplace=True)

    print("API data extracted")
    return df