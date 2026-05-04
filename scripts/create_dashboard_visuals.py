from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DASHBOARD_DIR = ROOT / "dashboard"
DASHBOARD_DIR.mkdir(exist_ok=True)


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
    columns=["customerNumber", "orderNumber", "amount", "paymentMethod"],
)


def build_model() -> pd.DataFrame:
    df = (
        order_details.merge(orders, on="orderNumber")
        .merge(products, on="productCode")
        .merge(customers, on="customerNumber")
        .merge(employees, left_on="salesRepEmployeeNumber", right_on="employeeNumber", how="left")
        .merge(offices, on="officeCode", how="left")
    )
    df["lineRevenue"] = df["quantitiesOrdered"] * df["priceOfEach"]
    df["orderDate"] = pd.to_datetime(df["orderDate"])
    return df


def create_png_dashboard(df: pd.DataFrame) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    fig = plt.figure(figsize=(18, 11))
    fig.suptitle("Car Company Database Dashboard", fontsize=22, fontweight="bold")

    total_revenue = df["lineRevenue"].sum()
    total_orders = df["orderNumber"].nunique()
    total_customers = df["customerNumber"].nunique()
    aov = total_revenue / total_orders

    ax0 = fig.add_subplot(3, 4, 1)
    ax0.axis("off")
    ax0.text(0, 0.82, "Total Revenue", fontsize=12, color="#555")
    ax0.text(0, 0.62, f"${total_revenue:,.0f}", fontsize=24, fontweight="bold")
    ax0.text(0, 0.42, "Orders", fontsize=12, color="#555")
    ax0.text(0, 0.25, f"{total_orders}", fontsize=22, fontweight="bold")
    ax0.text(0, 0.08, f"Customers: {total_customers} | AOV: ${aov:,.0f}", fontsize=11)

    ax1 = fig.add_subplot(3, 4, 2)
    df.groupby("productName")["lineRevenue"].sum().sort_values(ascending=False).plot(kind="bar", ax=ax1, color="#2f6f9f")
    ax1.set_title("Revenue by Product")
    ax1.set_xlabel("")
    ax1.set_ylabel("Revenue")

    ax2 = fig.add_subplot(3, 4, 3)
    df.groupby("status")["orderNumber"].nunique().plot(kind="bar", ax=ax2, color="#f28e2b")
    ax2.set_title("Orders by Status")
    ax2.set_xlabel("")
    ax2.set_ylabel("Orders")

    ax3 = fig.add_subplot(3, 4, 4)
    products.assign(stockStatus=products["quantityInStock"].le(15).map({True: "Low Stock", False: "Healthy"})).groupby("stockStatus")["productCode"].count().plot(kind="bar", ax=ax3, color="#e15759")
    ax3.set_title("Inventory Health")
    ax3.set_xlabel("")
    ax3.set_ylabel("Products")

    ax4 = fig.add_subplot(3, 4, 5)
    df.groupby("customerName")["lineRevenue"].sum().sort_values().plot(kind="barh", ax=ax4, color="#59a14f")
    ax4.set_title("Customer Revenue")
    ax4.set_xlabel("Revenue")

    ax5 = fig.add_subplot(3, 4, 6)
    df.groupby("employeeName")["lineRevenue"].sum().sort_values().plot(kind="barh", ax=ax5, color="#76b7b2")
    ax5.set_title("Employee Sales Contribution")
    ax5.set_xlabel("Revenue")

    ax6 = fig.add_subplot(3, 4, 7)
    df.groupby("officeCity")["lineRevenue"].sum().sort_values().plot(kind="barh", ax=ax6, color="#af7aa1")
    ax6.set_title("Office Revenue")
    ax6.set_xlabel("Revenue")

    ax7 = fig.add_subplot(3, 4, 8)
    payments.groupby("paymentMethod")["amount"].sum().sort_values(ascending=False).plot(kind="bar", ax=ax7, color="#edc948")
    ax7.set_title("Payments by Method")
    ax7.set_xlabel("")
    ax7.set_ylabel("Amount")

    ax8 = fig.add_subplot(3, 2, 5)
    monthly = df.groupby(df["orderDate"].dt.to_period("M"))["lineRevenue"].sum()
    monthly.index = monthly.index.astype(str)
    monthly.plot(kind="line", marker="o", ax=ax8, color="#4e79a7")
    ax8.set_title("Monthly Revenue Trend")
    ax8.set_xlabel("Month")
    ax8.set_ylabel("Revenue")

    ax9 = fig.add_subplot(3, 2, 6)
    payment_summary = payments.groupby("orderNumber")["amount"].sum().reset_index()
    order_summary = df.groupby("orderNumber")["lineRevenue"].sum().reset_index()
    reconciliation = order_summary.merge(payment_summary, on="orderNumber", how="left").fillna(0)
    reconciliation["balanceDue"] = reconciliation["lineRevenue"] - reconciliation["amount"]
    reconciliation.set_index("orderNumber")[["lineRevenue", "amount"]].plot(kind="bar", ax=ax9, color=["#9c755f", "#bab0ab"])
    ax9.set_title("Order Total vs Paid Amount")
    ax9.set_xlabel("Order Number")
    ax9.set_ylabel("Amount")

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(DASHBOARD_DIR / "car_company_dashboard.png", dpi=180)
    plt.close(fig)


def create_html_dashboard(df: pd.DataFrame) -> None:
    total_revenue = df["lineRevenue"].sum()
    total_orders = df["orderNumber"].nunique()
    total_customers = df["customerNumber"].nunique()
    paid_amount = payments["amount"].sum()

    tables = {
        "Product Revenue": df.groupby("productName")["lineRevenue"].sum().sort_values(ascending=False).reset_index(),
        "Customer Revenue": df.groupby("customerName")["lineRevenue"].sum().sort_values(ascending=False).reset_index(),
        "Employee Revenue": df.groupby("employeeName")["lineRevenue"].sum().sort_values(ascending=False).reset_index(),
        "Low Stock Products": products[products["quantityInStock"] <= 15],
        "Payment by Method": payments.groupby("paymentMethod")["amount"].sum().sort_values(ascending=False).reset_index(),
    }
    table_html = "\n".join(
        f"<section><h2>{title}</h2>{table.to_html(index=False, classes='data-table')}</section>"
        for title, table in tables.items()
    )
    html = f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Car Company Dashboard</title>
      <style>
        body {{ font-family: Arial, sans-serif; margin: 32px; color: #1f2933; background: #f7f9fb; }}
        .cards {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 24px; }}
        .card {{ background: white; border: 1px solid #d9e2ec; padding: 18px; border-radius: 8px; }}
        .card span {{ display: block; color: #52606d; font-size: 13px; }}
        .card strong {{ display: block; font-size: 24px; margin-top: 8px; }}
        img {{ max-width: 100%; border: 1px solid #d9e2ec; border-radius: 8px; background: white; }}
        section {{ background: white; border: 1px solid #d9e2ec; border-radius: 8px; padding: 18px; margin-top: 18px; }}
        .data-table {{ border-collapse: collapse; width: 100%; }}
        .data-table th, .data-table td {{ border-bottom: 1px solid #e5e7eb; padding: 8px; text-align: left; }}
      </style>
    </head>
    <body>
      <h1>Car Company Database Dashboard</h1>
      <div class="cards">
        <div class="card"><span>Total Revenue</span><strong>${total_revenue:,.0f}</strong></div>
        <div class="card"><span>Total Orders</span><strong>{total_orders}</strong></div>
        <div class="card"><span>Total Customers</span><strong>{total_customers}</strong></div>
        <div class="card"><span>Total Paid</span><strong>${paid_amount:,.0f}</strong></div>
      </div>
      <img src="car_company_dashboard.png" alt="Car company dashboard">
      {table_html}
    </body>
    </html>
    """
    (DASHBOARD_DIR / "car_company_dashboard.html").write_text(html, encoding="utf-8")


def main() -> None:
    df = build_model()
    create_png_dashboard(df)
    create_html_dashboard(df)
    print("Created car company dashboard PNG and HTML.")


if __name__ == "__main__":
    main()
