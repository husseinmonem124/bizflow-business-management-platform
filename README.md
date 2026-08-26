# BIZFLOW — Business Management Platform

BIZFLOW is a business management platform developed using **Python and SQLite**.

The system is designed to help a small business manage customers, products, inventory, orders, and basic business performance metrics from a single application.

## Business Problem

Small businesses often manage customers, products, and orders using disconnected spreadsheets or manual processes.

BIZFLOW provides a centralized system for managing these operations and generating useful business information.

## Features

### Customer Management

* Add customers
* Search customers
* View all customers
* Activate and deactivate customers
* View customer purchase history
* Calculate total customer spending
* Calculate number of customer orders
* Classify customers by spending level

### Product & Inventory Management

* Add products
* Search products
* View all products
* Update stock levels
* Automatically reduce stock after an order
* Low-stock alerts

### Order Management

* Create orders
* Search orders by customer
* View all orders
* Calculate order totals
* Apply a 10% discount to orders of 5 or more units
* Automatically update inventory after an order
* Display order history

### Business Dashboard

The dashboard provides key business performance indicators, including:

* Total orders
* Items sold
* Total revenue
* Average items per order
* Average order value
* Total customers
* Active customers
* Inactive customers
* Total products
* Items currently in stock
* Low-stock products

## Customer Analysis

BIZFLOW provides customer-level business information such as:

* Purchase history
* Total amount spent
* Number of orders
* Customer tier

Customers are classified according to their total spending:

| Spending     | Customer Tier    |
| ------------ | ---------------- |
| Below €500   | Regular Customer |
| €500–€999.99 | Valued Customer  |
| €1,000+      | VIP Customer     |

## Technologies

* **Python**
* **SQLite**
* **SQL**
* **sqlite3**
* **VS Code**
* **Git**
* **GitHub**

## Database

BIZFLOW uses SQLite to store business data.

The database contains three main tables:

* `customers`
* `products`
* `orders`

The tables are connected using foreign keys so that orders can be associated with both customers and products.

The Python application communicates with the database using Python's built-in `sqlite3` module.

## Project Structure

```text
bizflow-business-management-platform/
│
├── README.md
├── bizflow.py
├── database.py
└── bizflow.db
```

### `bizflow.py`

The main BIZFLOW application. It contains the customer, product, order, inventory, sales, and dashboard functionality.

### `database.py`

The database initialization script. It creates the required SQLite tables and inserts the initial product and customer data.

### `bizflow.db`

The SQLite database containing the application's stored business data.

### `README.md`

Project documentation explaining the purpose, functionality, technologies, and structure of BIZFLOW.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/husseinmonem124/bizflow-business-management-platform.git
```

### 2. Open the project folder

```bash
cd bizflow-business-management-platform
```

### 3. Initialize the database

Run:

```bash
python database.py
```

This creates or updates the `bizflow.db` SQLite database.

### 4. Run BIZFLOW

```bash
python bizflow.py
```

The application will start in the terminal and display the available management options.

## Example Workflow

A typical workflow is:

```text
Customer Management
        ↓
Select Customer
        ↓
Product Search
        ↓
Select Product
        ↓
Enter Quantity
        ↓
Calculate Order
        ↓
Save Order
        ↓
Update Inventory
        ↓
Generate Receipt
        ↓
Update Business Information
```

## Business KPIs

BIZFLOW demonstrates how operational data can be transformed into business information.

For example:

**Orders + Product Prices → Revenue**

**Orders + Quantities → Items Sold**

**Customer Orders → Customer Spending**

**Product Stock → Inventory Monitoring**

These metrics can help a small business monitor its operations and identify areas that may require attention.

## Input Validation

The system includes validation for several user inputs, including:

* Invalid quantities
* Negative stock amounts
* Negative product prices
* Invalid product selections
* Invalid customer selections
* Insufficient inventory
* Invalid numeric input

## Future Improvements

Possible future versions of BIZFLOW could include:

* User authentication
* Different user roles and permissions
* REST API
* Web-based frontend
* More advanced analytics
* Expense management
* Profit calculations
* Data visualization
* Exporting reports
* Automated backups
* Improved error handling
* Unit and integration testing

## What I Learned

Through this project, I practiced:

* Python programming
* SQL queries
* SQLite database management
* Relational database concepts
* CRUD operations
* Foreign keys
* Input validation
* Business KPI calculations
* Inventory management
* Customer analysis
* Order processing
* Basic software project structure
* Git and GitHub

## Project Status

**Version 1.0 — Completed**

BIZFLOW currently operates as a terminal-based business management application using Python and SQLite.
