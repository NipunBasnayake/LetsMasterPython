import mysql.connector

# Connect to MySQL and select the database
mydb = mysql.connector.connect(
    host="localhost",       # MySQL server host
    user="root",            # MySQL username
    password="1234",        # MySQL password
    database="my_database"  # Database to use
)

# Create a cursor object to execute SQL queries
my_cursor = mydb.cursor()

# Example 1: Parameterized query to safely select customers from Colombo
sql1 = "SELECT * FROM customers WHERE address = %s"
address = ("Colombo", )
my_cursor.execute(sql1, address)
result1 = my_cursor.fetchall()  # Fetch all rows

# Print results of the first query
print("Customers with address 'Colombo':")
for row in result1:
    # row contains (name, address, email)
    print(row)

# Example 2: Simple query with exact match
sql2 = "SELECT * FROM customers WHERE address = 'Colombo'"
my_cursor.execute(sql2)
result2 = my_cursor.fetchall()  # Fetch all rows

# Print results of the second query
print("\nCustomers with address 'Colombo' (second query):")
for row in result2:
    print(row)

# Close the cursor and database connection
my_cursor.close()
mydb.close()
