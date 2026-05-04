from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def build_data():
    offices = pd.DataFrame(
        [
            (4568, "Austin", "USA"),
            (4569, "Chicago", "USA"),
            (4567, "Newark", "USA"),
            (4570, "Connecticut", "USA"),
            (4571, "Colorado", "USA"),
        ],
        columns=["officeCode", "officeCity", "country"],
    )
    employees = pd.DataFrame(
        [
            (12345, "John Carter", "Sales Manager", 4568),
            (12346, "Sam Wilson", "Product Technician", 4569),
            (12347, "Kathy Smith", "Product Technician", 4567),
            (12348, "Simmer Ray", "Owner", 4570),
            (12349, "Sim Brown", "Project Manager", 4571),
        ],
        columns=["employeeNumber", "employeeName", "jobTitle", "officeCode"],
    )
    customers = pd.DataFrame(
        [
            (234, "Harry Jackson", "Austin", 12345),
            (235, "James Harrison", "Houston", 12345),
            (236, "Giri Patel", "San Diego", 12346),
            (237, "Anvesh Rao", "Texas", 12349),
            (238, "Siri Mehta", "San Francisco", 12347),
            (239, "Maria Lopez", "Chicago", 12346),
            (240, "David Kim", "Denver", 12349),
        ],
        columns=["customerNumber", "customerName", "city", "salesRepEmployeeNumber"],
    )
    products = pd.DataFrame(
        [
            (1, "Texus RX", 10, 23456.00),
            (2, "Texus LX", 40, 23478.00),
            (3, "Texus MX", 20, 23490.00),
            (4, "Texus UX", 50, 23498.00),
            (5, "Texus YX", 60, 23497.00),
            (6, "Texus Sport", 8, 38450.00),
            (7, "Texus EV", 15, 42400.00),
        ],
        columns=["productCode", "productName", "quantityInStock", "priceOfProduct"],
    )
    orders = pd.DataFrame(
        [
            (1, "2020-09-09", 234, "Shipped"),
            (2, "2020-03-09", 235, "Pending"),
            (3, "2020-04-09", 236, "Shipped"),
            (4, "2020-05-09", 234, "Shipped"),
            (5, "2020-04-09", 237, "Shipped"),
            (6, "2020-07-15", 238, "In Process"),
            (7, "2020-08-21", 239, "On Hold"),
            (8, "2020-11-03", 240, "Shipped"),
        ],
        columns=["orderNumber", "orderDate", "customerNumber", "status"],
    )
    order_details = pd.DataFrame(
        [
            (1, 1, 1, 2, 23456.00),
            (2, 2, 2, 3, 23478.00),
            (3, 3, 1, 4, 23456.00),
            (4, 4, 4, 5, 23498.00),
            (5, 5, 5, 5, 23497.00),
            (6, 6, 6, 1, 38450.00),
            (7, 7, 7, 2, 42400.00),
            (8, 8, 3, 1, 23490.00),
            (9, 8, 5, 1, 23497.00),
        ],
        columns=["orderLineNumber", "orderNumber", "productCode", "quantitiesOrdered", "priceOfEach"],
    )
    payments = pd.DataFrame(
        [
            (234, 1, 46912.00, "Credit Card"),
            (235, 2, 35000.00, "Bank Transfer"),
            (236, 3, 93824.00, "Credit Card"),
            (234, 4, 117490.00, "Wire Transfer"),
            (237, 5, 117485.00, "Credit Card"),
            (238, 6, 20000.00, "Debit Card"),
            (239, 7, 50000.00, "Bank Transfer"),
            (240, 8, 46987.00, "Credit Card"),
        ],
        columns=["customerNumber", "orderNumber", "paidAmount", "paymentMethod"],
    )
    sales = (
        order_details.merge(orders, on="orderNumber")
        .merge(products, on="productCode")
        .merge(customers, on="customerNumber")
        .merge(employees, left_on="salesRepEmployeeNumber", right_on="employeeNumber", how="left")
        .merge(offices, on="officeCode", how="left")
    )
    sales["lineRevenue"] = sales["quantitiesOrdered"] * sales["priceOfEach"]
    return sales, products, payments


def main():
    sales, products, payments = build_data()

    product_revenue = (
        sales.groupby("productName")
        .agg(unitsSold=("quantitiesOrdered", "sum"), revenue=("lineRevenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
    customer_revenue = (
        sales.groupby("customerName")
        .agg(orders=("orderNumber", "nunique"), revenue=("lineRevenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
    employee_revenue = (
        sales.groupby("employeeName")
        .agg(customers=("customerNumber", "nunique"), orders=("orderNumber", "nunique"), revenue=("lineRevenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
    office_revenue = (
        sales.groupby("officeCity")
        .agg(customers=("customerNumber", "nunique"), revenue=("lineRevenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
    order_status = (
        sales.groupby("status")
        .agg(orders=("orderNumber", "nunique"), revenue=("lineRevenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
    low_stock = products[products["quantityInStock"] <= 15].sort_values("quantityInStock")
    payment_method = (
        payments.groupby("paymentMethod")
        .agg(payments=("orderNumber", "count"), paidAmount=("paidAmount", "sum"))
        .sort_values("paidAmount", ascending=False)
    )

    outputs = {
        "product_revenue.csv": product_revenue,
        "customer_revenue.csv": customer_revenue,
        "employee_revenue.csv": employee_revenue,
        "office_revenue.csv": office_revenue,
        "order_status_summary.csv": order_status,
        "low_stock_products.csv": low_stock,
        "payment_method_summary.csv": payment_method,
    }
    for filename, table in outputs.items():
        table.to_csv(OUTPUT_DIR / filename)

    summary = f"""Car Company Database - Output Summary

Total revenue: ${sales['lineRevenue'].sum():,.2f}
Total orders: {sales['orderNumber'].nunique()}
Total customers: {sales['customerNumber'].nunique()}
Total products: {products['productCode'].nunique()}
Total paid amount: ${payments['paidAmount'].sum():,.2f}
Low-stock products: {len(low_stock)}

Top product by revenue: {product_revenue.index[0]} (${product_revenue.iloc[0]['revenue']:,.2f})
Top customer by revenue: {customer_revenue.index[0]} (${customer_revenue.iloc[0]['revenue']:,.2f})
Top employee by revenue handled: {employee_revenue.index[0]} (${employee_revenue.iloc[0]['revenue']:,.2f})
Top office by revenue: {office_revenue.index[0]} (${office_revenue.iloc[0]['revenue']:,.2f})
"""
    (OUTPUT_DIR / "project_output_summary.txt").write_text(summary, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
