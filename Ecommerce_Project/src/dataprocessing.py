import numpy as np
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "data" / "orders.csv"
data_path = BASE_DIR / "data" / "customers.csv"
data_path = BASE_DIR / "data" / "products.csv"

def load_data():
    customers = pd.read_csv('data/customers.csv')
    orders = pd.read_csv('data/order.csv')
    products = pd.read_csv('data/products.csv')
    return customers, orders, products


def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def load_data():
    customers , orders , products = load_data()
    customers = clean_data(customers),
    orders = clean_data(orders),
    products = clean_data(products)

    orders['order_date']= pd.to_datetime(
    orders['order_date']
    )
    return customers, orders, products


if __name__ == "__main__":
    customers, products, orders = clean_data()

    print("Customers:")
    print(customers.head())

    print("\nProducts:")
    print(products.head())

    print("\nOrders:")
    print(orders.head())


