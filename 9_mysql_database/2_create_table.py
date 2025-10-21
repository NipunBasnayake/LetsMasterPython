# Step 1: Import the MySQL Connector library
import mysql.connector
from mysql.connector import Error

# Step 2: Connect to the MySQL server and select an existing database
try:
    mydb = mysql.connector.connect(
        host="localhost",   # Your MySQL host (default: localhost)
        user="root",        # Your MySQL username
        password="1234",    # Your MySQL password
        database="my_database"  # The database you created earlier
    )

    if mydb.is_connected():
        print("✅ Successfully connected to MySQL and selected 'my_database'.")

except Error as e:
    print(f"❌ Error connecting to MySQL: {e}")

# Step 3: Create a cursor object to execute SQL commands
my_cursor = mydb.cursor()

# Step 4: Create a new table
try:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each customer
        name VARCHAR(255) NOT NULL,          -- Customer name
        address VARCHAR(255),                -- Customer address
        email VARCHAR(255) UNIQUE            -- Customer email (must be unique)
    )
    """
    my_cursor.execute(create_table_query)
    print("✅ Table 'customers' created successfully (or already exists).")

except Error as e:
    print(f"❌ Error creating table: {e}")

# Step 5: Show all tables in the selected database
print("\n📋 List of Tables in 'my_database':")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(" -", table[0])

# Step 6: Close the cursor and connection
my_cursor.close()
mydb.close()
print("\n🔒 Connection closed successfully.")
