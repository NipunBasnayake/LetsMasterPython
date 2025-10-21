import mysql.connector

# Connect to MySQL and select the database
mydb = mysql.connector.connect(
    host="localhost",       # MySQL server host
    user="root",            # MySQL username
    password="1234",        # MySQL password
    database="my_database"  # Database to use
)

my_cursor = mydb.cursor()

# Drop the 'customers' table if it exists
sql1 = "DROP TABLE IF EXISTS customers"
my_cursor.execute(sql1)
print("'customers' table dropped successfully (if it existed).")

# Close the cursor and database connection
my_cursor.close()
mydb.close()
