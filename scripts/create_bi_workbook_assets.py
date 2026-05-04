from pathlib import Path
from xml.sax.saxutils import escape

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DASHBOARD_DIR = ROOT / "dashboard"
DASHBOARD_DIR.mkdir(exist_ok=True)


def build_data() -> pd.DataFrame:
    offices = pd.DataFrame(
        [(4568, "Austin", "USA"), (4569, "Chicago", "USA"), (4567, "Newark", "USA"), (4570, "Connecticut", "USA"), (4571, "Colorado", "USA")],
        columns=["officeCode", "officeCity", "country"],
    )
    employees = pd.DataFrame(
        [(12345, "John Carter", "Sales Manager", 4568), (12346, "Sam Wilson", "Product Technician", 4569), (12347, "Kathy Smith", "Product Technician", 4567), (12348, "Simmer Ray", "Owner", 4570), (12349, "Sim Brown", "Project Manager", 4571)],
        columns=["employeeNumber", "employeeName", "jobTitle", "officeCode"],
    )
    customers = pd.DataFrame(
        [(234, "Harry Jackson", "Austin", 12345), (235, "James Harrison", "Houston", 12345), (236, "Giri Patel", "San Diego", 12346), (237, "Anvesh Rao", "Texas", 12349), (238, "Siri Mehta", "San Francisco", 12347), (239, "Maria Lopez", "Chicago", 12346), (240, "David Kim", "Denver", 12349)],
        columns=["customerNumber", "customerName", "city", "salesRepEmployeeNumber"],
    )
    products = pd.DataFrame(
        [(1, "Texus RX", 10, 23456.00), (2, "Texus LX", 40, 23478.00), (3, "Texus MX", 20, 23490.00), (4, "Texus UX", 50, 23498.00), (5, "Texus YX", 60, 23497.00), (6, "Texus Sport", 8, 38450.00), (7, "Texus EV", 15, 42400.00)],
        columns=["productCode", "productName", "quantityInStock", "priceOfProduct"],
    )
    orders = pd.DataFrame(
        [(1, "2020-09-09", 234, "Shipped"), (2, "2020-03-09", 235, "Pending"), (3, "2020-04-09", 236, "Shipped"), (4, "2020-05-09", 234, "Shipped"), (5, "2020-04-09", 237, "Shipped"), (6, "2020-07-15", 238, "In Process"), (7, "2020-08-21", 239, "On Hold"), (8, "2020-11-03", 240, "Shipped")],
        columns=["orderNumber", "orderDate", "customerNumber", "status"],
    )
    order_details = pd.DataFrame(
        [(1, 1, 1, 2, 23456.00), (2, 2, 2, 3, 23478.00), (3, 3, 1, 4, 23456.00), (4, 4, 4, 5, 23498.00), (5, 5, 5, 5, 23497.00), (6, 6, 6, 1, 38450.00), (7, 7, 7, 2, 42400.00), (8, 8, 3, 1, 23490.00), (9, 8, 5, 1, 23497.00)],
        columns=["orderLineNumber", "orderNumber", "productCode", "quantitiesOrdered", "priceOfEach"],
    )
    payments = pd.DataFrame(
        [(234, 1, 46912.00, "Credit Card"), (235, 2, 35000.00, "Bank Transfer"), (236, 3, 93824.00, "Credit Card"), (234, 4, 117490.00, "Wire Transfer"), (237, 5, 117485.00, "Credit Card"), (238, 6, 20000.00, "Debit Card"), (239, 7, 50000.00, "Bank Transfer"), (240, 8, 46987.00, "Credit Card")],
        columns=["customerNumber", "orderNumber", "paidAmount", "paymentMethod"],
    )
    df = (
        order_details.merge(orders, on="orderNumber")
        .merge(products, on="productCode")
        .merge(customers, on="customerNumber")
        .merge(employees, left_on="salesRepEmployeeNumber", right_on="employeeNumber", how="left")
        .merge(offices, on="officeCode", how="left")
        .merge(payments[["orderNumber", "paidAmount", "paymentMethod"]], on="orderNumber", how="left")
    )
    df["lineRevenue"] = df["quantitiesOrdered"] * df["priceOfEach"]
    df["balanceDue"] = df["lineRevenue"] - df["paidAmount"].fillna(0)
    return df


def write_twb(csv_path: Path, twb_path: Path) -> None:
    directory = escape(str(csv_path.parent))
    filename = escape(csv_path.name)
    xml = f"""<?xml version='1.0' encoding='utf-8' ?>
<workbook version='2024.1' source-build='2024.1.0'>
  <document-format-change-manifest />
  <datasources>
    <datasource caption='Car Company Dashboard Data' inline='true' name='car_company_dashboard_data' version='2024.1'>
      <connection class='textscan' directory='{directory}' filename='{filename}' password='' server='' />
      <column caption='Product Name' datatype='string' name='[productName]' role='dimension' type='nominal' />
      <column caption='Customer Name' datatype='string' name='[customerName]' role='dimension' type='nominal' />
      <column caption='Employee Name' datatype='string' name='[employeeName]' role='dimension' type='nominal' />
      <column caption='Office City' datatype='string' name='[officeCity]' role='dimension' type='nominal' />
      <column caption='Status' datatype='string' name='[status]' role='dimension' type='nominal' />
      <column caption='Line Revenue' datatype='real' name='[lineRevenue]' role='measure' type='quantitative' />
      <column caption='Paid Amount' datatype='real' name='[paidAmount]' role='measure' type='quantitative' />
      <column caption='Balance Due' datatype='real' name='[balanceDue]' role='measure' type='quantitative' />
      <column caption='Quantity In Stock' datatype='integer' name='[quantityInStock]' role='measure' type='quantitative' />
      <column caption='Quantity Ordered' datatype='integer' name='[quantitiesOrdered]' role='measure' type='quantitative' />
    </datasource>
  </datasources>
  <worksheets>
    <worksheet name='Open Data Source'>
      <table>
        <view>
          <datasources>
            <datasource caption='Car Company Dashboard Data' name='car_company_dashboard_data' />
          </datasources>
        </view>
      </table>
    </worksheet>
  </worksheets>
  <dashboards>
    <dashboard name='Car Company Dashboard Starter'>
      <style />
      <zones />
    </dashboard>
  </dashboards>
</workbook>
"""
    twb_path.write_text(xml, encoding="utf-8")


def main() -> None:
    df = build_data()
    csv_path = DASHBOARD_DIR / "car_company_dashboard_data.csv"
    df.to_csv(csv_path, index=False)
    write_twb(csv_path, DASHBOARD_DIR / "car_company_tableau_starter.twb")
    print("Created Car Company dashboard CSV and Tableau TWB starter.")


if __name__ == "__main__":
    main()
