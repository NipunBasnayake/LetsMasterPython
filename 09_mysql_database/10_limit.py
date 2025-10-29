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

# Example 1: Retrieve the first 2 rows from the 'customers' table
my_cursor.execute("SELECT * FROM customers LIMIT 2")
result1 = my_cursor.fetchall()
print("First 2 rows:")
for row in result1:
    print(row)

# Example 2: Retrieve 2 rows starting from the 3rd row (OFFSET 2)
my_cursor.execute("SELECT * FROM customers LIMIT 2 OFFSET 2")
result2 = my_cursor.fetchall()
print("\nNext 2 rows (offset 2):")
for row in result2:
    print(row)

# Close the cursor and database connection
my_cursor.close()
mydb.close()
