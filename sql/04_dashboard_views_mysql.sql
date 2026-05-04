USE car_company_database;

CREATE OR REPLACE VIEW vw_order_line_revenue AS
SELECT
    c.customerNumber,
    c.customerName,
    e.employeeName,
    ofc.city AS officeCity,
    o.orderNumber,
    o.orderDate,
    o.status,
    p.productCode,
    p.productName,
    p.quantityInStock,
    od.quantitiesOrdered,
    od.priceOfEach,
    od.quantitiesOrdered * od.priceOfEach AS lineRevenue
FROM Customers c
JOIN Orders o ON c.customerNumber = o.customerNumber
JOIN OrderDetails od ON o.orderNumber = od.orderNumber
JOIN Products p ON od.productCode = p.productCode
LEFT JOIN Employees e ON c.salesRepEmployeeNumber = e.employeeNumber
LEFT JOIN Offices ofc ON e.officeCode = ofc.officeCode;

CREATE OR REPLACE VIEW vw_payment_reconciliation AS
SELECT
    o.orderNumber,
    c.customerName,
    SUM(od.quantitiesOrdered * od.priceOfEach) AS orderTotal,
    COALESCE(SUM(pay.amount), 0) AS paidAmount,
    SUM(od.quantitiesOrdered * od.priceOfEach) - COALESCE(SUM(pay.amount), 0) AS balanceDue
FROM Orders o
JOIN Customers c ON o.customerNumber = c.customerNumber
JOIN OrderDetails od ON o.orderNumber = od.orderNumber
LEFT JOIN Payments pay ON o.orderNumber = pay.orderNumber
GROUP BY o.orderNumber, c.customerName;
