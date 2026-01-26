from sqlalchemy import create_engine

def load_to_db(df):
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost:5432/"
    )

    # IMPORTANT: use a connection
    with engine.connect() as connection:
        df.to_sql(
            "sales",
            con=connection,
            if_exists="append",
            index=False
        )

    print("Data loaded into database")

def load_products(df):
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost:5432/salesdb"
    )

    with engine.begin() as connection:
        df.to_sql(
            "products",
            con=connection,
            if_exists="replace",
            index=False
        )

    print("Products data loaded")
