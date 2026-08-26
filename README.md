# BIZFLOW — Business Management Platform

BIZFLOW is a business management platform developed using Python and SQLite.

The system is designed to help a small business manage customers, products, inventory, orders and basic business performance metrics from a single application.

## Business Problem

Small businesses often manage customers, products and orders using disconnected spreadsheets or manual processes.

BIZFLOW provides a simple centralized system for managing these operations and generating useful business information.

## Features

- Customer management
- Add and search customers
- Activate and deactivate customers
- Product management
- Add and search products
- Inventory and stock management
- Order creation
- Automatic stock updates
- Bulk order discounts
- Customer purchase history
- Order history
- Sales history
- Customer spending analysis
- Customer classification
- Business dashboard
- Revenue calculations
- Average order value
- Low-stock alerts
- SQLite database integration
- Input validation

## Technologies

- Python
- SQLite
- SQL
- VS Code
- Git
- GitHub

## Database

BIZFLOW uses SQLite to store business data including:

- Customers
- Products
- Orders
- Inventory information

The database is connected directly to the Python application using Python's `sqlite3` module.

## Business KPIs

The dashboard provides several business performance indicators, including:

- Total orders
- Items sold
- Total revenue
- Average items per order
- Average order value
- Total customers
- Active customers
- Inactive customers
- Total products
- Items in stock
- Low-stock products

## Customer Analysis

The system also provides customer-level information such as:

- Purchase history
- Total amount spent
- Number of orders
- Customer tier

Customers can be classified as:

- Regular Customer
- Valued Customer
- VIP Customer

based on their total spending.

## Order Management

Users can:

1. Search orders by customer
2. View all orders
3. Review order totals
4. Review total items purchased
5. Review customer spending
