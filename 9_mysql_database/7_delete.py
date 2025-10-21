import mysql.connector

# Connect to MySQL and select the database
mydb = mysql.connector.connect(
    host="localhost",       # MySQL server host
    user="root",            # MySQL username
    password="1234",        # MySQL password
    database="my_database"  # Database to use
)

my_cursor = mydb.cursor()

# Example 1: Delete all customers with address 'colombo'
sql1 = "DELETE FROM customers WHERE address = 'colombo'"
my_cursor.execute(sql1)
mydb.commit()  # Commit the changes to the database
print(my_cursor.rowcount, "record(s) deleted where address is 'colombo'.")

# Example 2: Delete a customer by name using a parameterized query
sql2 = "DELETE FROM customers WHERE name = %s"
name = ("Nimal Fernando", )
my_cursor.execute(sql2, name)
mydb.commit()  # Commit the changes to the database
print(my_cursor.rowcount, "record(s) deleted where name is 'Nimal Fernando'.")

# Close the cursor and database connection
my_cursor.close()
mydb.close()
