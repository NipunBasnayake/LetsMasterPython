# Step 1: Import the MySQL Connector library
import mysql.connector
from mysql.connector import Error

# Step 2: Connect to MySQL server (no database selected yet)
try:
    mydb = mysql.connector.connect(
        host="localhost",   # Your MySQL host (default: localhost)
        user="root",        # Your MySQL username
        password="1234"     # Your MySQL password
    )

    # Check if the connection is successful
    if mydb.is_connected():
        print("✅ Connection successful!")

except Error as e:
    print(f"❌ Error connecting to MySQL: {e}")

# Step 3: Create a cursor object
my_cursor = mydb.cursor()

# Step 4: Create a new database
try:
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
    print("✅ Database 'my_database' created successfully (or already exists).")
except Error as e:
    print(f"❌ Error creating database: {e}")

# Step 5: Show all available databases
print("\n📋 List of Databases:")
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(" -", db[0])

# Step 6: Close the connection (good practice!)
my_cursor.close()
mydb.close()
print("\n🔒 Connection closed successfully.")
