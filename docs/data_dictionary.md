# Data Dictionary

## Offices

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| officeCode | INT | PK | Unique identifier for each office |
| city | VARCHAR(50) | | Office city |
| country | VARCHAR(50) | | Office country |
| phoneNumber | VARCHAR(20) | | Office contact number |
| postalCode | VARCHAR(15) | | Office postal code |

## Employees

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| employeeNumber | INT | PK | Unique employee identifier |
| employeeName | VARCHAR(75) | | Employee full name |
| phoneNumber | VARCHAR(20) | | Employee phone number |
| email | VARCHAR(100) | UK | Employee email address |
| jobTitle | VARCHAR(50) | | Employee role |
| officeCode | INT | FK | Office where employee works |

## Customers

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| customerNumber | INT | PK | Unique customer identifier |
| customerName | VARCHAR(100) | | Customer full name |
| customerAddress | VARCHAR(150) | | Customer address |
| phoneNumber | VARCHAR(20) | | Customer phone number |
| city | VARCHAR(50) | | Customer city |
| country | VARCHAR(50) | | Customer country |
| salesRepEmployeeNumber | INT | FK | Employee assigned to customer |

## Products

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| productCode | INT | PK | Unique product identifier |
| productName | VARCHAR(75) | | Product/model name |
| productDescription | VARCHAR(255) | | Product details |
| modelYear | INT | | Vehicle model year |
| quantityInStock | INT | | Available stock |
| priceOfProduct | DECIMAL(12,2) | | Listed product price |

## Orders

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| orderNumber | INT | PK | Unique order identifier |
| orderDate | DATE | | Date order was placed |
| customerNumber | INT | FK | Customer who placed order |
| status | VARCHAR(25) | | Order fulfillment status |
| shippingDate | DATE | | Date order was shipped |

## OrderDetails

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| orderLineNumber | INT | PK | Unique order line identifier |
| orderNumber | INT | FK | Related order |
| productCode | INT | FK | Product ordered |
| quantitiesOrdered | INT | | Quantity ordered |
| priceOfEach | DECIMAL(12,2) | | Selling price per product |

## Payments

| Column | Type | Key | Description |
| --- | --- | --- | --- |
| paymentId | INT | PK | Unique payment identifier |
| customerNumber | INT | FK | Customer making payment |
| orderNumber | INT | FK | Related order |
| paymentDate | DATE | | Date of payment |
| amount | DECIMAL(12,2) | | Payment amount |
| paymentMethod | VARCHAR(30) | | Payment method |
