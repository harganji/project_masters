IF DB_ID('CarCompanyDatabase') IS NULL
BEGIN
    CREATE DATABASE CarCompanyDatabase;
END;
GO

USE CarCompanyDatabase;
GO

IF OBJECT_ID('dbo.Payments', 'U') IS NOT NULL DROP TABLE dbo.Payments;
IF OBJECT_ID('dbo.OrderDetails', 'U') IS NOT NULL DROP TABLE dbo.OrderDetails;
IF OBJECT_ID('dbo.Orders', 'U') IS NOT NULL DROP TABLE dbo.Orders;
IF OBJECT_ID('dbo.Customers', 'U') IS NOT NULL DROP TABLE dbo.Customers;
IF OBJECT_ID('dbo.Products', 'U') IS NOT NULL DROP TABLE dbo.Products;
IF OBJECT_ID('dbo.Employees', 'U') IS NOT NULL DROP TABLE dbo.Employees;
IF OBJECT_ID('dbo.Offices', 'U') IS NOT NULL DROP TABLE dbo.Offices;
GO

CREATE TABLE dbo.Offices (
    officeCode INT NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    phoneNumber VARCHAR(20) NOT NULL,
    postalCode VARCHAR(15) NOT NULL,
    CONSTRAINT PK_Offices PRIMARY KEY (officeCode)
);

CREATE TABLE dbo.Employees (
    employeeNumber INT NOT NULL,
    employeeName VARCHAR(75) NOT NULL,
    phoneNumber VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    jobTitle VARCHAR(50) NOT NULL,
    officeCode INT NOT NULL,
    CONSTRAINT PK_Employees PRIMARY KEY (employeeNumber),
    CONSTRAINT UQ_Employees_Email UNIQUE (email),
    CONSTRAINT FK_Employees_Offices
        FOREIGN KEY (officeCode) REFERENCES dbo.Offices(officeCode)
);

CREATE TABLE dbo.Customers (
    customerNumber INT NOT NULL,
    customerName VARCHAR(100) NOT NULL,
    customerAddress VARCHAR(150) NOT NULL,
    phoneNumber VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    salesRepEmployeeNumber INT NULL,
    CONSTRAINT PK_Customers PRIMARY KEY (customerNumber),
    CONSTRAINT FK_Customers_Employees
        FOREIGN KEY (salesRepEmployeeNumber) REFERENCES dbo.Employees(employeeNumber)
);

CREATE TABLE dbo.Products (
    productCode INT NOT NULL,
    productName VARCHAR(75) NOT NULL,
    productDescription VARCHAR(255) NOT NULL,
    modelYear INT NOT NULL,
    quantityInStock INT NOT NULL,
    priceOfProduct DECIMAL(12, 2) NOT NULL,
    CONSTRAINT PK_Products PRIMARY KEY (productCode),
    CONSTRAINT CK_Products_Quantity CHECK (quantityInStock >= 0),
    CONSTRAINT CK_Products_Price CHECK (priceOfProduct > 0)
);

CREATE TABLE dbo.Orders (
    orderNumber INT NOT NULL,
    orderDate DATE NOT NULL,
    customerNumber INT NOT NULL,
    status VARCHAR(25) NOT NULL,
    shippingDate DATE NULL,
    CONSTRAINT PK_Orders PRIMARY KEY (orderNumber),
    CONSTRAINT FK_Orders_Customers
        FOREIGN KEY (customerNumber) REFERENCES dbo.Customers(customerNumber),
    CONSTRAINT CK_Orders_Status
        CHECK (status IN ('Shipped', 'Pending', 'Cancelled', 'In Process', 'On Hold'))
);

CREATE TABLE dbo.OrderDetails (
    orderLineNumber INT NOT NULL,
    orderNumber INT NOT NULL,
    productCode INT NOT NULL,
    quantitiesOrdered INT NOT NULL,
    priceOfEach DECIMAL(12, 2) NOT NULL,
    CONSTRAINT PK_OrderDetails PRIMARY KEY (orderLineNumber),
    CONSTRAINT FK_OrderDetails_Orders
        FOREIGN KEY (orderNumber) REFERENCES dbo.Orders(orderNumber),
    CONSTRAINT FK_OrderDetails_Products
        FOREIGN KEY (productCode) REFERENCES dbo.Products(productCode),
    CONSTRAINT CK_OrderDetails_Quantity CHECK (quantitiesOrdered > 0),
    CONSTRAINT CK_OrderDetails_Price CHECK (priceOfEach > 0)
);

CREATE TABLE dbo.Payments (
    paymentId INT IDENTITY(1,1) NOT NULL,
    customerNumber INT NOT NULL,
    orderNumber INT NULL,
    paymentDate DATE NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    paymentMethod VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Payments PRIMARY KEY (paymentId),
    CONSTRAINT FK_Payments_Customers
        FOREIGN KEY (customerNumber) REFERENCES dbo.Customers(customerNumber),
    CONSTRAINT FK_Payments_Orders
        FOREIGN KEY (orderNumber) REFERENCES dbo.Orders(orderNumber),
    CONSTRAINT CK_Payments_Amount CHECK (amount > 0)
);
GO
