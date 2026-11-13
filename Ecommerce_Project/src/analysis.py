import pandas as pd
import matplotlib.pyplot as plt

from dataprocessing import load_clean_data


def create_sales_data():
    customers, orders, products = load_clean_data()

    sales = orders.merge(customers, on="customer_id")
    sales = sales.merge(products, on="product_id")
    sales["total_price"] = sales["quantity"] * sales["price"]

    return sales


def total_revenue(sales):
    return sales["total_price"].sum()


def top_products(sales):
    result = sales.groupby(
        "product_name"
    )["quantity"].sum()

    return result.sort_values(ascending=False)


def top_customers(sales):
    result = sales.groupby(
        "name"
    )["total_price"].sum()

    return result.sort_values(ascending=False)


def category_revenue(sales):
    return sales.groupby(
        "category"
    )["total_price"].sum().sort_values(ascending=False)


def monthly_sales(sales):
    sales = sales.copy()

    sales["month"] = sales["order_date"].dt.to_period("M")

    return sales.groupby("month")["total_price"].sum()


def visualize_sales(sales):
    monthly = monthly_sales(sales)

    monthly.plot(
        kind="line",
        marker="o",
        figsize=(10, 5),
        title="Monthly Sales"
    )

    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid()
    plt.tight_layout()
    plt.show()


def main():
    sales = create_sales_data()

    print("\nComplete Sales Data:")
    print(sales.head())

    print("\nTotal Revenue:")
    print(total_revenue(sales))

    print("\nTop Selling Products:")
    print(top_products(sales))

    print("\nTop Customers:")
    print(top_customers(sales))

    print("\nCategory Revenue:")
    print(category_revenue(sales))

    print("\nMonthly Sales:")
    print(monthly_sales(sales))

    visualize_sales(sales)


if __name__ == "__main__":
    main()
