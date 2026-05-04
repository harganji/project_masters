# Car Company Database Management System

This repository recreates and upgrades a masters-level database project for a car company. The project designs a normalized relational database to manage customers, employees, offices, products, orders, order line items, and payments.

## Project Objective

The goal of this project is to design a reliable database system for a car company that can track customer purchases, product inventory, order fulfillment, employee assignments, office locations, and customer payments. The database supports operational reporting and business analysis such as sales performance, inventory status, customer payment behavior, and employee sales contribution.

## Business Scenario

A car company sells multiple car models through different offices. Customers place orders for one or more products, employees manage customer relationships, and payments are recorded against completed purchases. The company needs a structured database to avoid duplicate data, enforce relationships, and answer business questions through SQL.

## Key Business Questions

- Which products generate the highest sales revenue?
- Which customers have placed the most valuable orders?
- Which offices and employees contribute most to sales?
- Which orders are shipped, pending, cancelled, or delayed?
- Which products are low in stock and need replenishment?
- Are customer payments aligned with order totals?

## Database Entities

- `Offices`: Stores company office locations.
- `Employees`: Stores employee details and office assignment.
- `Customers`: Stores customer contact details and assigned sales representative.
- `Products`: Stores car product information, model year, stock, and price.
- `Orders`: Stores order headers, status, order date, and shipping date.
- `OrderDetails`: Stores products and quantities inside each order.
- `Payments`: Stores customer payment transactions.

## Repository Structure

```text
project_masters_car_company_database/
  sql/
    01_create_database_sql_server.sql
    02_insert_sample_data_sql_server.sql
    03_business_analysis_queries.sql
    mysql_version.sql
  docs/
    data_dictionary.md
    erd.md
    project_report.md
  outputs/
    business query output CSV files
  assets/
    original_pdf_summary.md
  README.md
```

## Tools Used

- SQL Server / T-SQL
- MySQL-compatible script
- Tableau dashboard starter workbook
- Power BI dashboard plan for future `.pbix` creation
- Relational database design
- ERD modeling
- Normalization
- Primary keys and foreign keys
- SQL joins, aggregation, CTEs, and window functions

## Project Improvements Over the Original

The original project document had the core table idea, but this rebuilt version improves the project by:

- Adding proper foreign key relationships
- Fixing data types such as phone numbers and monetary values
- Replacing weak one-to-one assumptions with realistic one-to-many relationships
- Adding identity keys where needed
- Adding payment tracking with order references
- Adding business analysis SQL queries
- Adding data dictionary and ERD documentation
- Providing both SQL Server and MySQL-compatible scripts

## How to Run in SQL Server

1. Open SQL Server Management Studio.
2. Run:

```sql
sql/01_create_database_sql_server.sql
```

3. Run:

```sql
sql/02_insert_sample_data_sql_server.sql
```

4. Run:

```sql
sql/03_business_analysis_queries.sql
```

## How to Run in MySQL

Run the single MySQL script:

```sql
sql/mysql_version.sql
```

## Sample Insights

- Revenue can be analyzed by product, customer, office, and employee.
- Low-stock products can be identified before inventory shortages occur.
- Pending and delayed orders can be monitored using order and shipping dates.
- Payment coverage can be compared against order totals.
- Employee sales contribution can be measured through assigned customers.

## Output Files

The project includes generated CSV outputs for the main business queries:

- [outputs/product_revenue.csv](outputs/product_revenue.csv)
- [outputs/customer_revenue.csv](outputs/customer_revenue.csv)
- [outputs/employee_revenue.csv](outputs/employee_revenue.csv)
- [outputs/office_revenue.csv](outputs/office_revenue.csv)
- [outputs/order_status_summary.csv](outputs/order_status_summary.csv)
- [outputs/low_stock_products.csv](outputs/low_stock_products.csv)
- [outputs/payment_method_summary.csv](outputs/payment_method_summary.csv)
- [outputs/project_output_summary.txt](outputs/project_output_summary.txt)

## Visualization Guide

This project includes Tableau-ready dashboard assets and a separate Power BI/Tableau dashboard guide:

[docs/visualization_guide_powerbi_tableau.md](docs/visualization_guide_powerbi_tableau.md)

The guide covers dashboard pages, KPIs, visuals, Power BI DAX measures, Tableau calculated fields, and presentation storytelling. A `.pbix` file can be created from the included dashboard data and Power BI guide, but this repository currently includes the Tableau starter workbook and dashboard preview files.

Dashboard files included:

- [dashboard/car_company_dashboard.png](dashboard/car_company_dashboard.png)
- [dashboard/car_company_dashboard.html](dashboard/car_company_dashboard.html)
- [dashboard/car_company_tableau_starter.twb](dashboard/car_company_tableau_starter.twb)
- [dashboard/car_company_dashboard_data.csv](dashboard/car_company_dashboard_data.csv)
- [dashboard/power_bi_pbix_creation_steps.md](dashboard/power_bi_pbix_creation_steps.md)

## Interview Summary

This project demonstrates the ability to design a normalized relational database from a business problem, implement it with SQL, enforce data integrity through constraints, populate sample records, and write analytical queries that support business decision-making.
