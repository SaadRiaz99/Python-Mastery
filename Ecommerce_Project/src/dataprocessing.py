import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_data():
    customers = pd.read_csv(DATA_DIR / "customer.csv")
    orders = pd.read_csv(DATA_DIR / "order.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    return customers, orders, products


def clean_data(df):
    df = df.dropna().drop_duplicates().copy()
    return df


def load_clean_data():
    customers, orders, products = load_data()
    customers = clean_data(customers)
    orders = clean_data(orders)
    products = clean_data(products)
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    return customers, orders, products


if __name__ == "__main__":
    customers, orders, products = load_clean_data()

    print("Customers:")
    print(customers.head())

    print("\nOrders:")
    print(orders.head())

    print("\nProducts:")
    print(products.head())


