# Car Company Database Management System

Relational database design and SQL analytics project for a car company, rebuilt from a masters-level database assignment and upgraded into a recruiter-ready portfolio case study.

## Portfolio Summary

This project designs a normalized database for a car company that tracks offices, employees, customers, products, orders, order details, and payments. It includes SQL Server and MySQL scripts, business analysis queries, ERD documentation, output CSVs, and Tableau-ready dashboard assets.

## Business Problem

A car company needs a structured database to manage products, customers, orders, payments, employees, and office locations. Without a relational design, the company would face duplicated data, weak reporting, inconsistent payment tracking, and limited visibility into sales and inventory performance.

## Repository Structure

```text
project_masters/
  sql/
  docs/
  dashboard/
  outputs/
  scripts/
  assets/
  README.md
```

## Business Questions Answered

- Which products generate the highest sales revenue?
- Which customers have placed the most valuable orders?
- Which employees and offices contribute most to sales?
- Which orders are shipped, pending, in process, or on hold?
- Which products are low in stock and need replenishment?
- Are customer payments aligned with order totals?

## Tools Used

- SQL Server / T-SQL
- MySQL-compatible SQL
- Relational database design
- ERD modeling
- Primary keys, foreign keys, and constraints
- SQL joins, CTEs, aggregation, and window functions
- Tableau starter workbook and dashboard assets
- Power BI dashboard planning for future `.pbix` creation

## Database Entities

- `Offices`: Company office locations
- `Employees`: Employee details and office assignment
- `Customers`: Customer contact details and assigned sales representative
- `Products`: Car model details, stock, and price
- `Orders`: Order headers, customer, date, status, and shipping date
- `OrderDetails`: Product line items inside each order
- `Payments`: Customer payment transactions

## Files Included

| File | Purpose |
| --- | --- |
| [`sql/01_create_database_sql_server.sql`](sql/01_create_database_sql_server.sql) | SQL Server database and table creation |
| [`sql/02_insert_sample_data_sql_server.sql`](sql/02_insert_sample_data_sql_server.sql) | SQL Server sample data inserts |
| [`sql/03_business_analysis_queries.sql`](sql/03_business_analysis_queries.sql) | Business analysis SQL queries |
| [`sql/04_dashboard_views_mysql.sql`](sql/04_dashboard_views_mysql.sql) | MySQL views for dashboarding |
| [`sql/mysql_version.sql`](sql/mysql_version.sql) | Full MySQL-compatible database build script |
| [`docs/data_dictionary.md`](docs/data_dictionary.md) | Table and column definitions |
| [`docs/erd.md`](docs/erd.md) | ERD documentation |
| [`docs/project_report.md`](docs/project_report.md) | Project report and explanation |
| [`docs/visualization_guide_powerbi_tableau.md`](docs/visualization_guide_powerbi_tableau.md) | Power BI/Tableau visualization guide |
| [`assets/original_pdf_summary.md`](assets/original_pdf_summary.md) | Summary of original masters project reference |
| [`dashboard/car_company_dashboard.png`](dashboard/car_company_dashboard.png) | Dashboard image preview |
| [`dashboard/car_company_dashboard.html`](dashboard/car_company_dashboard.html) | Browser-viewable dashboard preview |
| [`dashboard/car_company_tableau_starter.twb`](dashboard/car_company_tableau_starter.twb) | Tableau starter workbook |
| [`dashboard/car_company_dashboard_data.csv`](dashboard/car_company_dashboard_data.csv) | Dashboard-ready data extract |
| [`dashboard/power_bi_pbix_creation_steps.md`](dashboard/power_bi_pbix_creation_steps.md) | Steps to create the `.pbix` in Power BI Desktop |
| [`outputs/`](outputs/) | Business output tables and summary |
| [`scripts/`](scripts/) | Dashboard and output generation scripts |

## Database Design Improvements

The original assignment contained the core table idea. This rebuilt version improves it by:

- Adding proper primary key and foreign key relationships
- Fixing data types such as phone numbers and currency values
- Replacing unrealistic one-to-one assumptions with realistic one-to-many relationships
- Adding payment tracking with order references
- Adding SQL constraints for data quality
- Adding business analysis queries and dashboard outputs
- Adding ERD, data dictionary, and project report documentation

## SQL Analysis Included

- Customer order detail report
- Product revenue ranking
- Customer lifetime revenue
- Employee sales contribution
- Office revenue performance
- Payment reconciliation
- Low-stock product report
- Shipping performance
- Monthly revenue trend
- Pending and incomplete orders

## Dashboard and Visualization

This repository includes Tableau-ready dashboard assets and dashboard preview files. A Power BI `.pbix` can be created from the included dashboard data and Power BI guide, but the repository currently includes the Tableau starter workbook and visual preview files.

Dashboard preview files:

- [Car Company Dashboard PNG](dashboard/car_company_dashboard.png)
- [Car Company Dashboard HTML](dashboard/car_company_dashboard.html)
- [Tableau Starter Workbook](dashboard/car_company_tableau_starter.twb)
- [Dashboard Data CSV](dashboard/car_company_dashboard_data.csv)
- [Power BI PBIX Creation Steps](dashboard/power_bi_pbix_creation_steps.md)

## Output Summary

Generated outputs show:

- Total revenue: `$616,382.00`
- Total orders: `8`
- Total customers: `7`
- Total products: `7`
- Total paid amount: `$527,698.00`
- Low-stock products: `3`
- Top product by revenue: `Texus YX`
- Top customer by revenue: `Harry Jackson`
- Top employee by revenue handled: `John Carter`
- Top office by revenue: `Austin`

## How to Run

SQL Server:

```sql
sql/01_create_database_sql_server.sql
sql/02_insert_sample_data_sql_server.sql
sql/03_business_analysis_queries.sql
```

MySQL:

```sql
sql/mysql_version.sql
```

Generate dashboard/output assets:

```bash
python scripts/create_dashboard_visuals.py
python scripts/create_bi_workbook_assets.py
python scripts/generate_outputs.py
```

## Interview Story

I rebuilt this database project from an original academic assignment and upgraded it into a business-focused analytics project. I redesigned the schema, corrected relationships and data types, added SQL Server and MySQL implementations, created business reporting queries, generated output files, and built Tableau-ready dashboard assets.

This project demonstrates database design, SQL implementation, data integrity, business analysis, and dashboard storytelling.
