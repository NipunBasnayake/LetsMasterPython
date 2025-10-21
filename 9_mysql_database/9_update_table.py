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

# Example 1: Update address from 'Matara' to 'Galle'
sql1 = "UPDATE customers SET address = 'Matara' WHERE address = 'Galle'"
my_cursor.execute(sql1)
mydb.commit()  # Commit the changes
print(my_cursor.rowcount, "record(s) updated.")

# Example 2: Update email for a specific customer using parameterized query
sql2 = "UPDATE customers SET address = %s WHERE address = %s"
values = ('Negombo', 'Kandy')  # Corrected: email value and name
my_cursor.execute(sql2, values)
mydb.commit()  # Commit the changes
print(my_cursor.rowcount, "record(s) updated.")

# Close the cursor and database connection
my_cursor.close()
mydb.close()
