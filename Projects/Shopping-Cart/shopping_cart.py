import csv
import os
from datetime import datetime

PRODUCTS_FILE = 'products.csv'
CART_FILE = 'cart.csv'

def initialize_files():
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'price', 'stock'])
            writer.writerow([1, 'Laptop', 999.99, 10])
            writer.writerow([2, 'Phone', 699.99, 25])
            writer.writerow([3, 'Headphones', 149.99, 50])
            writer.writerow([4, 'Mouse', 29.99, 100])
            writer.writerow([5, 'Keyboard', 79.99, 75])

def display_products():
    with open(PRODUCTS_FILE, 'r') as f:
        products = list(csv.DictReader(f))
    print('ID  Name              Price    Stock')
    print('-' * 40)
    for p in products:
        print(f'{p[\
