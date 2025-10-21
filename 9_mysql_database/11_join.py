import mysql.connector

# Connect to MySQL and select the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="my_database"
)

my_cursor = mydb.cursor()


# 1. INNER JOIN (only matching rows)

sql_inner = """
SELECT customers.name, orders.product
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
"""
my_cursor.execute(sql_inner)
inner_result = my_cursor.fetchall()
print("INNER JOIN (Customer Orders):")
for row in inner_result:
    print(row)
print()


# 2. LEFT JOIN (all customers, even if no order)

sql_left = """
SELECT customers.name, orders.product
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
"""
my_cursor.execute(sql_left)
left_result = my_cursor.fetchall()
print("LEFT JOIN (All Customers with Orders if exists):")
for row in left_result:
    print(row)
print()


# 3. RIGHT JOIN (all orders, even if no customer - for demo)

sql_right = """
SELECT customers.name, orders.product
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id
"""
my_cursor.execute(sql_right)
right_result = my_cursor.fetchall()
print("RIGHT JOIN (All Orders with Customer info if exists):")
for row in right_result:
    print(row)
print()


# 4. FULL OUTER JOIN simulation using UNION (MySQL doesn't support FULL OUTER JOIN directly)

sql_full = """
SELECT customers.name, orders.product
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
UNION
SELECT customers.name, orders.product
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id
"""
my_cursor.execute(sql_full)
full_result = my_cursor.fetchall()
print("FULL OUTER JOIN (All Customers and Orders):")
for row in full_result:
    print(row)
print()

# Close cursor and connection
my_cursor.close()
mydb.close()
