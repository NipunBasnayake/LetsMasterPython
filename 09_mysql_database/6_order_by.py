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

# Query 1: Select all names from 'users' in ascending order
sql1 = "SELECT name FROM customers ORDER BY name"
my_cursor.execute(sql1)
result1 = my_cursor.fetchall()  # Fetch all rows

print("Users in ascending order:")
for row in result1:
    print(row[0])  # row is a tuple, print first element (name)

# Query 2: Select all names from 'users' in descending order
sql2 = "SELECT name FROM customers ORDER BY name DESC"
my_cursor.execute(sql2)
result2 = my_cursor.fetchall()  # Fetch all rows

print("\nUsers in descending order:")
for row in result2:
    print(row[0])  # row is a tuple, print first element (name)

# Close the cursor and connection
my_cursor.close()
mydb.close()
