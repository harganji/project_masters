# Project Report - Car Company Database

## 1. Project Description

This project designs and implements a relational database for a car company. The company needs to store product information, customer information, orders, ordered products, payments, employees, and office locations. The system supports daily operations and analytical reporting.

## 2. Business Requirements

The database must allow the company to:

- Maintain a list of car products and available stock.
- Store customer contact and location details.
- Track customer orders and shipping status.
- Store multiple products within the same order.
- Record customer payments.
- Assign customers to employees.
- Connect employees to office locations.
- Produce sales, payment, inventory, and operational reports.

## 3. Tables

### Offices
Stores the different office locations of the company.

### Employees
Stores employee details and connects each employee to an office.

### Customers
Stores customer details and connects customers to their assigned sales representative.

### Products
Stores car model details, stock quantity, and product price.

### Orders
Stores order header information such as order date, customer, shipping date, and status.

### OrderDetails
Stores each product line within an order. This enables an order to include multiple products.

### Payments
Stores payment transactions made by customers, optionally tied to an order.

## 4. Normalization

The project follows relational design principles:

- Product details are stored once in `Products`.
- Customer details are stored once in `Customers`.
- Orders are separated into order headers and order line details.
- Employees and offices are separated to avoid repeating office data for every employee.
- Payments are separated from orders because an order can be paid through one or more transactions.

## 5. Relationship Summary

- Offices to Employees: one-to-many
- Employees to Customers: one-to-many
- Customers to Orders: one-to-many
- Orders to OrderDetails: one-to-many
- Products to OrderDetails: one-to-many
- Customers to Payments: one-to-many
- Orders to Payments: one-to-many

## 6. SQL Implementation

The SQL Server implementation includes:

- Database creation
- Table creation
- Primary keys
- Foreign keys
- Check constraints
- Unique email constraint
- Sample data inserts
- Business analysis queries

## 7. Business Queries Included

- Customer order detail report
- Product revenue ranking
- Customer lifetime revenue
- Employee sales contribution
- Office revenue performance
- Payment reconciliation
- Low-stock product report
- Shipping performance
- Monthly revenue trend
- Pending/incomplete orders

## 8. Conclusion

The recreated database project provides a complete and improved version of the original car company database. It demonstrates database design, SQL implementation, relationship modeling, data integrity, and business reporting.
