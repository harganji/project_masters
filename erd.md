# Entity Relationship Diagram

```mermaid
erDiagram
    OFFICES ||--o{ EMPLOYEES : employs
    EMPLOYEES ||--o{ CUSTOMERS : manages
    CUSTOMERS ||--o{ ORDERS : places
    ORDERS ||--o{ ORDERDETAILS : contains
    PRODUCTS ||--o{ ORDERDETAILS : ordered_as
    CUSTOMERS ||--o{ PAYMENTS : makes
    ORDERS ||--o{ PAYMENTS : paid_by

    OFFICES {
        int officeCode PK
        varchar city
        varchar country
        varchar phoneNumber
        varchar postalCode
    }

    EMPLOYEES {
        int employeeNumber PK
        varchar employeeName
        varchar phoneNumber
        varchar email UK
        varchar jobTitle
        int officeCode FK
    }

    CUSTOMERS {
        int customerNumber PK
        varchar customerName
        varchar customerAddress
        varchar phoneNumber
        varchar city
        varchar country
        int salesRepEmployeeNumber FK
    }

    PRODUCTS {
        int productCode PK
        varchar productName
        varchar productDescription
        int modelYear
        int quantityInStock
        decimal priceOfProduct
    }

    ORDERS {
        int orderNumber PK
        date orderDate
        int customerNumber FK
        varchar status
        date shippingDate
    }

    ORDERDETAILS {
        int orderLineNumber PK
        int orderNumber FK
        int productCode FK
        int quantitiesOrdered
        decimal priceOfEach
    }

    PAYMENTS {
        int paymentId PK
        int customerNumber FK
        int orderNumber FK
        date paymentDate
        decimal amount
        varchar paymentMethod
    }
```

## Relationship Explanation

- One office can have many employees.
- One employee can manage many customers.
- One customer can place many orders.
- One order can contain many order detail rows.
- One product can appear in many order detail rows.
- One customer can make many payments.
- One order can have zero, one, or many payment records.
