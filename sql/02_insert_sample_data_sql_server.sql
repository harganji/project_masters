USE CarCompanyDatabase;
GO

INSERT INTO dbo.Offices (officeCode, city, country, phoneNumber, postalCode)
VALUES
(4568, 'Austin', 'USA', '9876543734', '67689'),
(4569, 'Chicago', 'USA', '9887543734', '57689'),
(4567, 'Newark', 'USA', '9876983734', '87689'),
(4570, 'Connecticut', 'USA', '9576983734', '77687'),
(4571, 'Colorado', 'USA', '9476983734', '47689');

INSERT INTO dbo.Employees (employeeNumber, employeeName, phoneNumber, email, jobTitle, officeCode)
VALUES
(12345, 'John Carter', '9087867856', 'john.carter@texusauto.com', 'Sales Manager', 4568),
(12346, 'Sam Wilson', '9087877856', 'sam.wilson@texusauto.com', 'Product Technician', 4569),
(12347, 'Kathy Smith', '8087867856', 'kathy.smith@texusauto.com', 'Product Technician', 4567),
(12348, 'Simmer Ray', '9887867856', 'simmer.ray@texusauto.com', 'Owner', 4570),
(12349, 'Sim Brown', '9887867756', 'sim.brown@texusauto.com', 'Project Manager', 4571);

INSERT INTO dbo.Customers (customerNumber, customerName, customerAddress, phoneNumber, city, country, salesRepEmployeeNumber)
VALUES
(234, 'Harry Jackson', 'Jackson Street', '9874563423', 'Austin', 'USA', 12345),
(235, 'James Harrison', 'Harrison Street', '9764563423', 'Houston', 'USA', 12345),
(236, 'Giri Patel', 'Chicago Street', '9877863423', 'San Diego', 'USA', 12346),
(237, 'Anvesh Rao', 'Jefferson Street', '9877868423', 'Texas', 'USA', 12349),
(238, 'Siri Mehta', 'Town Street', '9677863423', 'San Francisco', 'USA', 12347),
(239, 'Maria Lopez', 'Market Street', '9677863123', 'Chicago', 'USA', 12346),
(240, 'David Kim', 'Lake Road', '9677863223', 'Denver', 'USA', 12349);

INSERT INTO dbo.Products (productCode, productName, productDescription, modelYear, quantityInStock, priceOfProduct)
VALUES
(1, 'Texus RX', 'Premium SUV model', 2019, 10, 23456.00),
(2, 'Texus LX', 'Luxury sedan model', 2018, 40, 23478.00),
(3, 'Texus MX', 'Compact crossover model', 2017, 20, 23490.00),
(4, 'Texus UX', 'Urban compact SUV model', 2016, 50, 23498.00),
(5, 'Texus YX', 'Family hybrid model', 2015, 60, 23497.00),
(6, 'Texus Sport', 'Performance sports model', 2020, 8, 38450.00),
(7, 'Texus EV', 'Electric vehicle model', 2021, 15, 42400.00);

INSERT INTO dbo.Orders (orderNumber, orderDate, customerNumber, status, shippingDate)
VALUES
(1, '2020-09-09', 234, 'Shipped', '2020-09-12'),
(2, '2020-03-09', 235, 'Pending', '2020-03-19'),
(3, '2020-04-09', 236, 'Shipped', '2020-04-10'),
(4, '2020-05-09', 234, 'Shipped', '2020-05-12'),
(5, '2020-04-09', 237, 'Shipped', '2020-04-12'),
(6, '2020-07-15', 238, 'In Process', NULL),
(7, '2020-08-21', 239, 'On Hold', NULL),
(8, '2020-11-03', 240, 'Shipped', '2020-11-08');

INSERT INTO dbo.OrderDetails (orderLineNumber, orderNumber, productCode, quantitiesOrdered, priceOfEach)
VALUES
(1, 1, 1, 2, 23456.00),
(2, 2, 2, 3, 23478.00),
(3, 3, 1, 4, 23456.00),
(4, 4, 4, 5, 23498.00),
(5, 5, 5, 5, 23497.00),
(6, 6, 6, 1, 38450.00),
(7, 7, 7, 2, 42400.00),
(8, 8, 3, 1, 23490.00),
(9, 8, 5, 1, 23497.00);

INSERT INTO dbo.Payments (customerNumber, orderNumber, paymentDate, amount, paymentMethod)
VALUES
(234, 1, '2020-09-09', 46912.00, 'Credit Card'),
(235, 2, '2020-03-10', 35000.00, 'Bank Transfer'),
(236, 3, '2020-04-09', 93824.00, 'Credit Card'),
(234, 4, '2020-05-09', 117490.00, 'Wire Transfer'),
(237, 5, '2020-04-09', 117485.00, 'Credit Card'),
(238, 6, '2020-07-16', 20000.00, 'Debit Card'),
(239, 7, '2020-08-22', 50000.00, 'Bank Transfer'),
(240, 8, '2020-11-04', 46987.00, 'Credit Card');
