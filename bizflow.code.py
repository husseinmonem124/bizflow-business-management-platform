# ========================================
# BIZFLOW - Business Management Platform
# ========================================

from builtins import print
from datetime import datetime
import sqlite3


# ---------- Business Information ----------

business_name = "Electronics Saga"
owner_name = "Joshua"

print("================================")
print("            BIZFLOW")
print("================================")
print("Business:", business_name)
print("Owner:", owner_name)


# ---------- Database Connection ----------

connection = sqlite3.connect("bizflow.db")
cursor = connection.cursor()


# ---------- Product Information ----------

cursor.execute("SELECT id, name, price FROM products")
products = cursor.fetchall()


# ---------- Customer Management ----------

print("\n========== CUSTOMER MANAGEMENT ==========")
print("1. Search customer")
print("2. Add customer")
print("3. View all customers")
print("4. Deactivate customer")
print("5. Reactivate customer")
print("6. Product Management")
print("7. Business Dashboard")

customer_option = input("\nChoose an option: ")


if customer_option == "6":

    print("\n========== PRODUCT MANAGEMENT ==========")
    print("1. Add product")
    print("2. View all products")
    print("3. Update stock")

    product_option = input("\nChoose an option: ")

    if product_option == "1":

        print("\n========== ADD PRODUCT ==========")

        product_name = input("Product name: ")
        product_price = float(input("Product price: €"))
        product_stock = int(input("Initial stock: "))

        if product_price < 0:
            print("Invalid price.")
            connection.close()
            exit()

        if product_stock < 0:
            print("Invalid stock amount.")
            connection.close()
            exit()

        cursor.execute(
            """
            INSERT INTO products (name, price, stock)
            VALUES (?, ?, ?)
            """,
            (product_name, product_price, product_stock)
        )

        connection.commit()

        product_id = cursor.lastrowid

        print("\nProduct added successfully!")
        print("Product ID:", product_id)
        print("Product:", product_name)
        print(f"Price: €{product_price:.2f}")
        print("Stock:", product_stock)

        connection.close()
        exit()

    if product_option == "2":

        print("\n========== ALL PRODUCTS ==========")

        cursor.execute(
            """
            SELECT id, name, price, stock
            FROM products
            ORDER BY name
            """
        )

        all_products = cursor.fetchall()

        for product in all_products:
            print(
                "ID:", product[0],
                "| Product:", product[1],
                f"| Price: €{product[2]:.2f}",
                "| Stock:", product[3]
            )

        connection.close()
        exit()

    if product_option == "3":

        print("\n========== UPDATE STOCK ==========")

        search_product = input("Search product: ")

        cursor.execute(
            """
            SELECT id, name, price, stock
            FROM products
            WHERE name LIKE ?
            """,
            ("%" + search_product + "%",)
        )

        matching_products = cursor.fetchall()

        if len(matching_products) == 0:
            print("No products found.")
            connection.close()
            exit()

        print("\nMatching Products:")

        for index, product in enumerate(matching_products, start=1):
            print(
                index,
                ".",
                product[1],
                "- Current stock:",
                product[3]
            )

        product_choice = int(input("\nChoose a product: "))

        while product_choice < 1 or product_choice > len(matching_products):
            print("Invalid product selection.")
            product_choice = int(input("Choose a product: "))

        selected_product = matching_products[product_choice - 1]

        product_id = selected_product[0]
        product_name = selected_product[1]
        current_stock = selected_product[3]

        print("\nSelected product:", product_name)
        print("Current stock:", current_stock)

        stock_to_add = int(
            input("How many units would you like to add? ")
        )

        while stock_to_add < 1:
            print("Invalid amount. Enter at least 1.")
            stock_to_add = int(
                input("How many units would you like to add? ")
            )

        new_stock = current_stock + stock_to_add

        cursor.execute(
            """
            UPDATE products
            SET stock = ?
            WHERE id = ?
            """,
            (new_stock, product_id)
        )

        connection.commit()

        print("\nStock updated successfully!")
        print("Product:", product_name)
        print("Previous stock:", current_stock)
        print("Added:", stock_to_add)
        print("New stock:", new_stock)

        connection.close()
        exit()

if customer_option == "4":

    print("\n========== DEACTIVATE CUSTOMER ==========")

    search_name = input("Search customer to deactivate: ")

    cursor.execute(
        """
        SELECT id, name, email, status
        FROM customers
        WHERE name LIKE ?
        """,
        ("%" + search_name + "%",)
    )

    matching_customers = cursor.fetchall()

    if len(matching_customers) == 0:
        print("No customers found.")
        connection.close()
        exit()

    print("\nMatching Customers:")

    for index, customer in enumerate(matching_customers, start=1):
        print(
            index,
            ".",
            customer[1],
            "-",
            customer[2],
            "- Status:",
            customer[3]
        )

    customer_choice = int(input("\nChoose a customer: "))

    while customer_choice < 1 or customer_choice > len(matching_customers):
        print("Invalid customer selection.")
        customer_choice = int(input("Choose a customer: "))

    selected_customer = matching_customers[customer_choice - 1]

    customer_id = selected_customer[0]
    customer_name = selected_customer[1]

    print("\nSelected customer:", customer_name)

    confirmation = input("Deactivate this customer? (yes/no): ")

    if confirmation.lower() == "yes":

        cursor.execute(
            """
            UPDATE customers
            SET status = 'Inactive'
            WHERE id = ?
            """,
            (customer_id,)
        )

        connection.commit()

        print("\nCustomer deactivated successfully!")

    else:
        print("\nCustomer was not deactivated.")

    connection.close()
    exit()

if customer_option == "5":

    print("\n========== REACTIVATE CUSTOMER ==========")

    search_name = input("Search customer to reactivate: ")

    cursor.execute(
        """
        SELECT id, name, email, status
        FROM customers
        WHERE name LIKE ?
        """,
        ("%" + search_name + "%",)
    )

    matching_customers = cursor.fetchall()

    if len(matching_customers) == 0:
        print("No customers found.")
        connection.close()
        exit()

    print("\nMatching Customers:")

    for index, customer in enumerate(matching_customers, start=1):
        print(
            index,
            ".",
            customer[1],
            "-",
            customer[2],
            "- Status:",
            customer[3]
        )

    customer_choice = int(input("\nChoose a customer: "))

    while customer_choice < 1 or customer_choice > len(matching_customers):
        print("Invalid customer selection.")
        customer_choice = int(input("Choose a customer: "))

    selected_customer = matching_customers[customer_choice - 1]

    customer_id = selected_customer[0]
    customer_name = selected_customer[1]

    print("\nSelected customer:", customer_name)

    confirmation = input("Reactivate this customer? (yes/no): ")

    if confirmation.lower() == "yes":

        cursor.execute(
            """
            UPDATE customers
            SET status = 'Active'
            WHERE id = ?
            """,
            (customer_id,)
        )

        connection.commit()

        print("\nCustomer reactivated successfully!")

    else:
        print("\nCustomer was not reactivated.")

    connection.close()
    exit()
    
if customer_option == "3":

    print("\n========== ALL CUSTOMERS ==========")

    cursor.execute("SELECT id, name, email, status FROM customers")

    all_customers = cursor.fetchall()

    for customer in all_customers:
     print(
        "ID:", customer[0],
        "| Name:", customer[1],
        "| Email:", customer[2],
        "| Status:", customer[3]
    )

    connection.close()
    exit()

if customer_option == "2":

    print("\n========== ADD CUSTOMER ==========")

    new_customer_name = input("Customer name: ")
    new_customer_email = input("Customer email: ")

    cursor.execute(
        """
        INSERT INTO customers (name, email)
        VALUES (?, ?)
        """,
        (new_customer_name, new_customer_email)
    )

    connection.commit()

    customer_id = cursor.lastrowid
    customer_name = new_customer_name
    customer_email = new_customer_email

    print("\nCustomer added successfully!")
    print("Customer ID:", customer_id)

else:

    print("\n========== CUSTOMER SEARCH ==========")

    search_name = input("Search customer: ")

    cursor.execute(
        """
        SELECT id, name, email, status
        FROM customers
        WHERE name LIKE ?
        """,
        ("%" + search_name + "%",)
    )

    matching_customers = cursor.fetchall()

    if len(matching_customers) == 0:
        print("No customers found.")
        connection.close()
        exit()

    print("\nMatching Customers:")

    for index, customer in enumerate(matching_customers, start=1):
        print(index, ".", customer[1], "-", customer[2], "- Status:", customer[3])
    customer_choice = int(input("\nChoose a customer: "))

    while customer_choice < 1 or customer_choice > len(matching_customers):
        print("Invalid customer selection.")
        customer_choice = int(input("Choose a customer: "))

    selected_customer = matching_customers[customer_choice - 1]

    customer_id = selected_customer[0]
    customer_name = selected_customer[1]
    customer_email = selected_customer[2]
    customer_status = selected_customer[3]

    print("\nSelected customer:", customer_name)
    print("Email:", customer_email)
    print("Status:", customer_status)

    print("\n========== PURCHASE HISTORY ==========")

cursor.execute(
    """
    SELECT
        orders.id,
        products.name,
        products.price,
        orders.quantity,
        orders.order_date
    FROM orders
    JOIN products
        ON orders.product_id = products.id
    WHERE orders.customer_id = ?
    ORDER BY orders.id
    """,
    (customer_id,)
)

customer_orders = cursor.fetchall()

if len(customer_orders) == 0:
    print("No purchase history found.")
else:
    for order in customer_orders:

        order_id = order[0]
        product = order[1]
        price = order[2]
        quantity = order[3]
        order_date = order[4]

        order_total = price * quantity

        if quantity >= 5:
            order_total = order_total * 0.90

        print("\nOrder #", order_id)
        print("Date:", order_date)
        print("Product:", product)
        print("Quantity:", quantity)
        print(f"Total: €{order_total:.2f}")
customer_total_spent = 0

for order in customer_orders:

    price = order[2]
    quantity = order[3]

    order_total = price * quantity

    if quantity >= 5:
        order_total = order_total * 0.90

    customer_total_spent = customer_total_spent + order_total

print(f"\nTotal Spent by Customer: €{customer_total_spent:.2f}")
cursor.execute(
    """
    SELECT COUNT(*)
    FROM orders
    WHERE customer_id = ?
    """,
    (customer_id,)
)

customer_order_count = cursor.fetchone()[0]

print("Total Orders by Customer:", customer_order_count)
if customer_total_spent >= 1000:
    customer_tier = "VIP Customer"
elif customer_total_spent >= 500:
    customer_tier = "Valued Customer"
else:
    customer_tier = "Regular Customer"

print("Customer Tier:", customer_tier)

if customer_status != "Active":
        print("\nThis customer is inactive and cannot place a new order.")
        connection.close()
        exit()
    


# ---------- Functions ----------

def calculate_order(price, quantity):
    total = price * quantity

    if quantity >= 5:
        discount = total * 0.10
        total = total - discount
        print("Discount applied: 10%")
    else:
        print("No discount applied.")

    return total


# ---------- Product Search ----------

print("\n========== PRODUCT SEARCH ==========")

search_product = input("Search product: ")

cursor.execute(
    """
    SELECT id, name, price, stock
    FROM products
    WHERE name LIKE ?
    """,
    ("%" + search_product + "%",)
)

matching_products = cursor.fetchall()

if len(matching_products) == 0:
    print("No products found.")
    connection.close()
    exit()

print("\nMatching Products:")

for index, product in enumerate(matching_products, start=1):
    print(
        index,
        ".",
        product[1],
        "- €",
        product[2],
        "- Stock:",
        product[3]
    )

choice = int(input("\nChoose a product: "))

while choice < 1 or choice > len(matching_products):
    print("Invalid product selection.")
    choice = int(input("Choose a product: "))

selected_product = matching_products[choice - 1]

product_id = selected_product[0]
product_name = selected_product[1]
product_price = selected_product[2]
product_stock = selected_product[3]

print("\nSelected product:", product_name)
print("Price: €", product_price)
print("Stock available:", product_stock)
print("\n========== SALES HISTORY ==========")

cursor.execute(
    """
    SELECT
        SUM(quantity),
        COUNT(*)
    FROM orders
    WHERE product_id = ?
    """,
    (product_id,)
)

sales_data = cursor.fetchone()

units_sold = sales_data[0] or 0
orders_containing_product = sales_data[1] or 0

print("Units Sold:", units_sold)
print("Orders Containing Product:", orders_containing_product)
cursor.execute(
    """
    SELECT
        SUM(products.price * orders.quantity)
    FROM orders
    JOIN products
        ON orders.product_id = products.id
    WHERE orders.product_id = ?
    """,
    (product_id,)
)

product_revenue = cursor.fetchone()[0] or 0

print(f"Product Revenue: €{product_revenue:.2f}")

# ---------- Order ----------

while True:

    try:
        quantity = int(input("How many would you like? "))

        if quantity < 1:
            print("Invalid quantity. Please enter at least 1.")
            continue

        if quantity > product_stock:
            print("Not enough stock available.")
            print("Available stock:", product_stock)
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("Quantity:", quantity)

total = calculate_order(product_price, quantity)
# ---------- Save Order ----------

order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.execute(
    """
    INSERT INTO orders (customer_id, product_id, quantity, order_date)
    VALUES (?, ?, ?, ?)
    """,
    (customer_id, product_id, quantity, order_date)
)

# ---------- Update Stock ----------

cursor.execute(
    """
    UPDATE products
    SET stock = stock - ?
    WHERE id = ?
    """,
    (quantity, product_id)
)

connection.commit()

order_id = cursor.lastrowid

print("\nOrder saved successfully!")

print("Stock updated!")

cursor.execute(
    "SELECT stock FROM products WHERE id = ?",
    (product_id,)
)

remaining_stock = cursor.fetchone()[0]

print("Remaining stock:", remaining_stock)

if remaining_stock <= 5:
    print("WARNING: Low stock!")


# ---------- Receipt ----------

print("\n================================")
print("          BIZFLOW RECEIPT")
print("================================")

print("Order ID:", order_id)
print("Order Date:", order_date)
print("Customer:", customer_name)
print("Email:", customer_email)
print("Product:", product_name)
print("Quantity:", quantity)
print("Remaining Stock:", remaining_stock)

original_total = product_price * quantity
discount_amount = original_total - total

print(f"Original Total: €{original_total:.2f}")

if discount_amount > 0:
    print(f"Discount: €{discount_amount:.2f}")

print(f"Final Total: €{total:.2f}")
print("================================")


# ---------- Order History ----------

cursor.execute("""
SELECT
    orders.id,
    customers.name,
    products.name,
    products.price,
    orders.quantity,
    orders.order_date
FROM orders
JOIN customers
    ON orders.customer_id = customers.id
JOIN products
    ON orders.product_id = products.id
""")

order_history = cursor.fetchall()

print("\n========== ORDER HISTORY ==========")

for order in order_history:

    order_id = order[0]
    customer = order[1]
    product = order[2]
    price = order[3]
    quantity = order[4]
    order_date = order[5]

    total = price * quantity

    if quantity >= 5:
        total = total * 0.90

    print("\nOrder #", order_id)
    print("Date:", order_date)
    print("Customer:", customer)
    print("Product:", product)
    print("Quantity:", quantity)
    print(f"Total: €{total:.2f}")

# ---------- Order Management ----------

print("\n========== ORDER MANAGEMENT ==========")
print("1. Search orders")
print("2. View all orders")

order_option = input("\nChoose an option: ")
if order_option == "2":

    print("\n========== ALL ORDERS ==========")

    cursor.execute("""
    SELECT
        orders.id,
        customers.name,
        products.name,
        products.price,
        orders.quantity,
        orders.order_date
    FROM orders
    JOIN customers
        ON orders.customer_id = customers.id
    JOIN products
        ON orders.product_id = products.id
    ORDER BY orders.id
    """)

    all_orders = cursor.fetchall()

    if len(all_orders) == 0:
        print("No orders found.")
    else:
        for order in all_orders:

            order_id = order[0]
            customer = order[1]
            product = order[2]
            price = order[3]
            quantity = order[4]
            order_date = order[5]

            total = price * quantity

            if quantity >= 5:
                total = total * 0.90

            print("\nOrder #", order_id)
            print("Date:", order_date)
            print("Customer:", customer)
            print("Product:", product)
            print("Quantity:", quantity)
            print(f"Total: €{total:.2f}")

        print("\n========== ORDER SUMMARY ==========")

    total_all_orders = len(all_orders)
    total_all_items = 0
    total_all_revenue = 0

    for order in all_orders:

        quantity = order[4]
        price = order[3]

        total_all_items = total_all_items + quantity

        order_total = price * quantity

        if quantity >= 5:
            order_total = order_total * 0.90

        total_all_revenue = total_all_revenue + order_total

    print("Total Orders:", total_all_orders)
    print("Total Items Sold:", total_all_items)
    print(f"Total Revenue: €{total_all_revenue:.2f}")

    connection.close()
    exit()

if order_option == "1":

    print("\n========== SEARCH ORDERS ==========")

    search_customer = input("Search customer: ")

    cursor.execute(
        """
        SELECT
            orders.id,
            customers.name,
            products.name,
            products.price,
            orders.quantity,
            orders.order_date
        FROM orders
        JOIN customers
            ON orders.customer_id = customers.id
        JOIN products
            ON orders.product_id = products.id
        WHERE customers.name LIKE ?
        ORDER BY orders.id
        """,
        ("%" + search_customer + "%",)
    )

    matching_orders = cursor.fetchall()

    if len(matching_orders) == 0:
        print("No orders found for this customer.")
        connection.close()
        exit()

    print("\nMatching Orders:")

    for order in matching_orders:

        order_id = order[0]
        customer = order[1]
        product = order[2]
        price = order[3]
        quantity = order[4]
        order_date = order[5]

        total = price * quantity

        if quantity >= 5:
            total = total * 0.90

        print("\nOrder #", order_id)
        print("Date:", order_date)
        print("Customer:", customer)
        print("Product:", product)
        print("Quantity:", quantity)
        print(f"Total: €{total:.2f}")

        print("\n========== CUSTOMER ORDER SUMMARY ==========")

    total_customer_orders = len(matching_orders)
    total_customer_items = 0
    total_customer_spent = 0

    for order in matching_orders:

        quantity = order[4]
        price = order[3]

        total_customer_items = total_customer_items + quantity

        order_total = price * quantity

        if quantity >= 5:
            order_total = order_total * 0.90

        total_customer_spent = total_customer_spent + order_total

    print("Total Orders:", total_customer_orders)
    print("Total Items Purchased:", total_customer_items)
    print(f"Total Spent: €{total_customer_spent:.2f}")

    connection.close()
    exit()

# ---------- Business Dashboard ----------

cursor.execute("SELECT COUNT(*) FROM orders")
total_orders = cursor.fetchone()[0]

print("\n================================")
print("       BIZFLOW DASHBOARD")
print("================================")
print("Total Orders:", total_orders)
cursor.execute("SELECT SUM(quantity) FROM orders")
total_items = cursor.fetchone()[0]

print("Items Sold:", total_items)
if total_orders > 0:
    average_items_per_order = total_items / total_orders
else:
    average_items_per_order = 0

print(f"Average Items Per Order: {average_items_per_order:.2f}")
cursor.execute("""
SELECT SUM(products.price * orders.quantity)
FROM orders
JOIN products
    ON orders.product_id = products.id
""")

total_revenue = cursor.fetchone()[0]

print(f"Total Revenue: €{total_revenue:.2f}")
if total_orders > 0:
    average_order_value = total_revenue / total_orders
else:
    average_order_value = 0

print(f"Average Order Value: €{average_order_value:.2f}")

cursor.execute("SELECT COUNT(*) FROM customers")
total_customers = cursor.fetchone()[0]

print("Total Customers:", total_customers)

cursor.execute(
    "SELECT COUNT(*) FROM customers WHERE status = 'Active'"
)

active_customers = cursor.fetchone()[0]

print("Active Customers:", active_customers)

cursor.execute(
    "SELECT COUNT(*) FROM customers WHERE status = 'Inactive'"
)

inactive_customers = cursor.fetchone()[0]

print("Inactive Customers:", inactive_customers)

cursor.execute("SELECT COUNT(*) FROM products")

total_products = cursor.fetchone()[0]

print("Total Products:", total_products)

cursor.execute("SELECT SUM(stock) FROM products")

total_stock = cursor.fetchone()[0]

print("Total Items In Stock:", total_stock)

cursor.execute(
    """
    SELECT name, stock
    FROM products
    WHERE stock <= 5
    """
)

low_stock_products = cursor.fetchall()

print("\nLOW STOCK ALERTS")

if len(low_stock_products) == 0:
    print("No low-stock products.")
else:
    for product in low_stock_products:
        print(product[0], "-", product[1], "remaining")

# ---------- Close Database ----------

connection.close()

print("\nDatabase connection closed.")