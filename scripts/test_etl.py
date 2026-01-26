from extract_api import extract_api
from load import load_products

df = extract_api()
load_products(df)