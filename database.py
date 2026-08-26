import sqlite3
from datetime import datetime


# ========================================
# BIZFLOW DATABASE
# ========================================

# ---------- Database Connection ----------

connection = sqlite3.connect("bizflow.db")

connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

print("Database connected!")


# ========================================
# PRODUCTS
# ========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price REAL,
    stock INTEGER
)
""")

products_to_add = [
    ("Laptop", 899, 10),
    ("Monitor", 299, 20),
    ("Keyboard", 79, 50)
]

cursor.executemany(
    "INSERT OR IGNORE INTO products (name, price, stock) VALUES (?, ?, ?)",
    products_to_add
)

connection.commit()

print("Products added!")


# ---------- Display Products ----------

cursor.execute("SELECT id, name, price FROM products")

products = cursor.fetchall()

print("\nProducts in database:")

for product in products:
    print(product)


# ---------- Find Expensive Products ----------

cursor.execute(
    "SELECT name, price FROM products WHERE price > ?",
    (500,)
)

expensive_products = cursor.fetchall()

print("\nProducts over €500:")

for product in expensive_products:
    print(product)


# ========================================
# CUSTOMERS
# ========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    email TEXT,
    status TEXT DEFAULT 'Active'
)
""")
cursor.execute("PRAGMA table_info(customers)")
customer_columns = cursor.fetchall()

print("\nCustomer table columns:")

for column in customer_columns:
    print(column)

customers_to_add = [
    ("Werner Kimmich", "werner@example.com", "Active"),
    ("Anna Scholl", "anna@example.com", "Active"),
    ("Hans Havertz", "hanshavertz@example.com", "Active"),
    ("Magdalena Neuer", "magdalenaneuer@example.com", "Active"),
    ("Mario Beckenbaur", "mariobeck@example.com", "Active"),
    ("Stella Schurlle", "stellaschurll@example.com", "Active"),
    ("Thomas Muller", "thomasmuller@example.com", "Active"),
    ("Thomas Wirtz", "thomaswirtz@example.com", "Active"),
    ("Giesela Schertling", "gieselaschertling@example.com", "Active")
]

cursor.executemany(
    """
    INSERT OR IGNORE INTO customers (name, email, status)
    VALUES (?, ?, ?)
    """,
    customers_to_add
)

connection.commit()

print("\nCustomers added!")


# ---------- Display Customers ----------

cursor.execute("SELECT id, name, email, status FROM customers")

customers = cursor.fetchall()

print("\nCustomers in database:")

for customer in customers:
    print(customer)


# ========================================
# ORDERS
# ========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

connection.commit()

print("\nOrders table ready!")


# ---------- Display Orders ----------

cursor.execute("""
SELECT id, customer_id, product_id, quantity, order_date
FROM orders
""")

orders = cursor.fetchall()

print("\nOrders in database:")

for order in orders:
    print(order)


# ========================================
# ORDER DETAILS
# ========================================

cursor.execute("""
SELECT
    orders.id,
    customers.name,
    products.name,
    orders.quantity,
    orders.order_date
FROM orders
JOIN customers
    ON orders.customer_id = customers.id
JOIN products
    ON orders.product_id = products.id
""")

order_details = cursor.fetchall()

print("\nOrder Details:")

for order in order_details:
    print(order)


# ---------- Close Database ----------

connection.close()

print("\nDatabase connection closed.")
