# Visualization Guide - Power BI and Tableau

This guide explains how to build dashboards for the Car Company Database project in Power BI and Tableau.

## Data Source

Use the SQL scripts in:

```text
sql/
```

Recommended source for dashboards:

- SQL Server database: `CarCompanyDatabase`
- MySQL database: `car_company_database`

Tables:

- `Offices`
- `Employees`
- `Customers`
- `Products`
- `Orders`
- `OrderDetails`
- `Payments`

## Dashboard Goal

Help the car company understand sales performance, customer value, inventory risk, employee contribution, office performance, order status, and payment completion.

## Suggested Dashboard Pages

### Page 1: Executive Sales Overview

Purpose:
Summarize sales revenue and order performance.

KPIs:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Shipped Orders
- Pending/In-Process Orders

Visuals:

- KPI cards: total revenue, orders, customers, AOV
- Bar chart: revenue by product
- Column chart: monthly revenue trend
- Donut chart: order status distribution
- Table: top customers by revenue

Business question answered:
How is the company performing overall, and which products/customers drive revenue?

### Page 2: Product and Inventory Performance

Purpose:
Show product-level sales and inventory status.

KPIs:

- Units Sold
- Products in Stock
- Low-Stock Products
- Top Product Revenue

Visuals:

- Bar chart: product revenue ranking
- Bar chart: units sold by product
- Table: low-stock products
- Scatter plot: product price vs units sold
- Matrix: product by order status

Business question answered:
Which car models are selling, and which models need inventory attention?

### Page 3: Customer and Payment Analysis

Purpose:
Analyze customer value and payment completion.

KPIs:

- Paid Amount
- Balance Due
- Fully Paid Orders
- Partially Paid Orders

Visuals:

- Bar chart: customer lifetime revenue
- Table: order payment reconciliation
- Stacked bar chart: order total vs paid amount
- Bar chart: payment amount by method
- Table: customers with unpaid or partially paid balances

Business question answered:
Which customers are most valuable, and where does the company need payment follow-up?

### Page 4: Office and Employee Performance

Purpose:
Measure operational contribution by office and employee.

KPIs:

- Revenue by Office
- Revenue by Employee
- Assigned Customers
- Orders Handled

Visuals:

- Bar chart: employee sales contribution
- Map: revenue by office city
- Bar chart: office revenue performance
- Table: employee, office, customers, orders, revenue

Business question answered:
Which offices and employees contribute most to company performance?

## Power BI Model Design

Recommended relationships:

- `Offices[officeCode]` -> `Employees[officeCode]`
- `Employees[employeeNumber]` -> `Customers[salesRepEmployeeNumber]`
- `Customers[customerNumber]` -> `Orders[customerNumber]`
- `Orders[orderNumber]` -> `OrderDetails[orderNumber]`
- `Products[productCode]` -> `OrderDetails[productCode]`
- `Customers[customerNumber]` -> `Payments[customerNumber]`
- `Orders[orderNumber]` -> `Payments[orderNumber]`

Set relationship direction to single where possible, from dimension tables to fact tables.

## Power BI Measures

```DAX
Total Revenue =
SUMX(
    OrderDetails,
    OrderDetails[quantitiesOrdered] * OrderDetails[priceOfEach]
)

Total Orders =
DISTINCTCOUNT(Orders[orderNumber])

Total Customers =
DISTINCTCOUNT(Customers[customerNumber])

Average Order Value =
DIVIDE([Total Revenue], [Total Orders])

Units Sold =
SUM(OrderDetails[quantitiesOrdered])

Total Paid Amount =
SUM(Payments[amount])

Balance Due =
[Total Revenue] - [Total Paid Amount]

Shipped Orders =
CALCULATE(
    DISTINCTCOUNT(Orders[orderNumber]),
    Orders[status] = "Shipped"
)

Pending Orders =
CALCULATE(
    DISTINCTCOUNT(Orders[orderNumber]),
    Orders[status] IN {"Pending", "In Process", "On Hold"}
)

Low Stock Products =
CALCULATE(
    DISTINCTCOUNT(Products[productCode]),
    Products[quantityInStock] <= 15
)
```

## Power BI Calculated Columns

```DAX
Order Line Revenue =
OrderDetails[quantitiesOrdered] * OrderDetails[priceOfEach]
```

```DAX
Shipping Days =
DATEDIFF(Orders[orderDate], Orders[shippingDate], DAY)
```

```DAX
Stock Status =
IF(
    Products[quantityInStock] <= 15,
    "Low Stock",
    "Healthy Stock"
)
```

```DAX
Payment Status =
IF(
    [Balance Due] <= 0,
    "Paid",
    "Needs Follow-up"
)
```

## Tableau Build Instructions

### Recommended Tableau Data Model

Connect to SQL Server or MySQL and relate tables using:

- Offices to Employees on `officeCode`
- Employees to Customers on `employeeNumber = salesRepEmployeeNumber`
- Customers to Orders on `customerNumber`
- Orders to OrderDetails on `orderNumber`
- Products to OrderDetails on `productCode`
- Orders to Payments on `orderNumber`

### Tableau Calculated Fields

```text
Order Line Revenue
[quantitiesOrdered] * [priceOfEach]
```

```text
Total Revenue
SUM([Order Line Revenue])
```

```text
Average Order Value
SUM([Order Line Revenue]) / COUNTD([orderNumber])
```

```text
Units Sold
SUM([quantitiesOrdered])
```

```text
Total Paid Amount
SUM([amount])
```

```text
Stock Status
IF [quantityInStock] <= 15 THEN "Low Stock"
ELSE "Healthy Stock"
END
```

```text
Shipping Days
DATEDIFF('day', [orderDate], [shippingDate])
```

```text
Order Status Group
IF [status] = "Shipped" THEN "Completed"
ELSE "Open / Needs Attention"
END
```

### Tableau Sheets

Create these sheets:

- KPI - Total Revenue
- KPI - Total Orders
- KPI - Average Order Value
- Product Revenue Ranking
- Monthly Revenue Trend
- Order Status Distribution
- Top Customers by Revenue
- Low Stock Products
- Payment Reconciliation
- Employee Sales Contribution
- Office Revenue Map

### Tableau Dashboard Layout

Dashboard 1: Sales Overview

- KPI row at the top
- Product revenue ranking on the left
- Monthly trend on the right
- Order status and top customers at the bottom

Dashboard 2: Inventory and Orders

- Low-stock KPI
- Low-stock table
- Product revenue vs units sold
- Pending/in-process order table

Dashboard 3: Payments and Operations

- Paid amount and balance due KPIs
- Payment reconciliation table
- Employee revenue contribution
- Office revenue map

## Storytelling Flow

Use this narrative in presentations:

1. The database organizes company operations into customers, products, orders, payments, employees, and offices.
2. Sales performance can be tracked by product, customer, employee, and office.
3. Inventory risk is visible through low-stock reporting.
4. Payment reconciliation identifies orders that need finance follow-up.
5. The dashboard turns the database project into a business intelligence system.
