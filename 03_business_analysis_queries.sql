USE CarCompanyDatabase;
GO

-- 1. View all customer orders with product details
SELECT
    c.customerNumber,
    c.customerName,
    o.orderNumber,
    o.orderDate,
    o.status,
    p.productName,
    od.quantitiesOrdered,
    od.priceOfEach,
    od.quantitiesOrdered * od.priceOfEach AS lineRevenue
FROM dbo.Customers c
JOIN dbo.Orders o
    ON c.customerNumber = o.customerNumber
JOIN dbo.OrderDetails od
    ON o.orderNumber = od.orderNumber
JOIN dbo.Products p
    ON od.productCode = p.productCode
ORDER BY o.orderNumber, od.orderLineNumber;

-- 2. Product revenue ranking using window functions
WITH product_sales AS (
    SELECT
        p.productCode,
        p.productName,
        SUM(od.quantitiesOrdered) AS unitsSold,
        SUM(od.quantitiesOrdered * od.priceOfEach) AS revenue
    FROM dbo.Products p
    JOIN dbo.OrderDetails od
        ON p.productCode = od.productCode
    GROUP BY p.productCode, p.productName
)
SELECT
    productCode,
    productName,
    unitsSold,
    revenue,
    RANK() OVER (ORDER BY revenue DESC) AS revenueRank
FROM product_sales
ORDER BY revenueRank;

-- 3. Customer lifetime revenue
SELECT
    c.customerNumber,
    c.customerName,
    COUNT(DISTINCT o.orderNumber) AS totalOrders,
    SUM(od.quantitiesOrdered * od.priceOfEach) AS customerRevenue
FROM dbo.Customers c
JOIN dbo.Orders o
    ON c.customerNumber = o.customerNumber
JOIN dbo.OrderDetails od
    ON o.orderNumber = od.orderNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY customerRevenue DESC;

-- 4. Employee sales contribution
SELECT
    e.employeeNumber,
    e.employeeName,
    e.jobTitle,
    COUNT(DISTINCT c.customerNumber) AS assignedCustomers,
    COUNT(DISTINCT o.orderNumber) AS ordersHandled,
    COALESCE(SUM(od.quantitiesOrdered * od.priceOfEach), 0) AS revenueHandled
FROM dbo.Employees e
LEFT JOIN dbo.Customers c
    ON e.employeeNumber = c.salesRepEmployeeNumber
LEFT JOIN dbo.Orders o
    ON c.customerNumber = o.customerNumber
LEFT JOIN dbo.OrderDetails od
    ON o.orderNumber = od.orderNumber
GROUP BY e.employeeNumber, e.employeeName, e.jobTitle
ORDER BY revenueHandled DESC;

-- 5. Office-level revenue performance
SELECT
    ofc.officeCode,
    ofc.city,
    ofc.country,
    COUNT(DISTINCT e.employeeNumber) AS employees,
    COUNT(DISTINCT c.customerNumber) AS customers,
    COALESCE(SUM(od.quantitiesOrdered * od.priceOfEach), 0) AS officeRevenue
FROM dbo.Offices ofc
LEFT JOIN dbo.Employees e
    ON ofc.officeCode = e.officeCode
LEFT JOIN dbo.Customers c
    ON e.employeeNumber = c.salesRepEmployeeNumber
LEFT JOIN dbo.Orders o
    ON c.customerNumber = o.customerNumber
LEFT JOIN dbo.OrderDetails od
    ON o.orderNumber = od.orderNumber
GROUP BY ofc.officeCode, ofc.city, ofc.country
ORDER BY officeRevenue DESC;

-- 6. Order payment reconciliation
WITH order_totals AS (
    SELECT
        o.orderNumber,
        o.customerNumber,
        SUM(od.quantitiesOrdered * od.priceOfEach) AS orderTotal
    FROM dbo.Orders o
    JOIN dbo.OrderDetails od
        ON o.orderNumber = od.orderNumber
    GROUP BY o.orderNumber, o.customerNumber
),
payment_totals AS (
    SELECT
        orderNumber,
        SUM(amount) AS paidAmount
    FROM dbo.Payments
    GROUP BY orderNumber
)
SELECT
    ot.orderNumber,
    c.customerName,
    ot.orderTotal,
    COALESCE(pt.paidAmount, 0) AS paidAmount,
    ot.orderTotal - COALESCE(pt.paidAmount, 0) AS balanceDue,
    CASE
        WHEN COALESCE(pt.paidAmount, 0) >= ot.orderTotal THEN 'Paid'
        WHEN COALESCE(pt.paidAmount, 0) > 0 THEN 'Partially Paid'
        ELSE 'Unpaid'
    END AS paymentStatus
FROM order_totals ot
JOIN dbo.Customers c
    ON ot.customerNumber = c.customerNumber
LEFT JOIN payment_totals pt
    ON ot.orderNumber = pt.orderNumber
ORDER BY balanceDue DESC;

-- 7. Low-stock products
SELECT
    productCode,
    productName,
    modelYear,
    quantityInStock,
    priceOfProduct
FROM dbo.Products
WHERE quantityInStock <= 15
ORDER BY quantityInStock ASC;

-- 8. Order shipping performance
SELECT
    orderNumber,
    orderDate,
    shippingDate,
    status,
    DATEDIFF(DAY, orderDate, shippingDate) AS daysToShip
FROM dbo.Orders
WHERE shippingDate IS NOT NULL
ORDER BY daysToShip DESC;

-- 9. Monthly revenue trend
SELECT
    YEAR(o.orderDate) AS orderYear,
    MONTH(o.orderDate) AS orderMonth,
    COUNT(DISTINCT o.orderNumber) AS orders,
    SUM(od.quantitiesOrdered * od.priceOfEach) AS revenue
FROM dbo.Orders o
JOIN dbo.OrderDetails od
    ON o.orderNumber = od.orderNumber
GROUP BY YEAR(o.orderDate), MONTH(o.orderDate)
ORDER BY orderYear, orderMonth;

-- 10. Customers with pending or incomplete orders
SELECT
    c.customerNumber,
    c.customerName,
    o.orderNumber,
    o.orderDate,
    o.status,
    o.shippingDate
FROM dbo.Customers c
JOIN dbo.Orders o
    ON c.customerNumber = o.customerNumber
WHERE o.status IN ('Pending', 'In Process', 'On Hold')
ORDER BY o.orderDate;
