# Step 1: Import the MySQL Connector library
import mysql.connector
from mysql.connector import Error

# Step 2: Connect to the MySQL server and select your database
try:
    mydb = mysql.connector.connect(
        host="localhost",   # Your MySQL host (default: localhost)
        user="root",        # Your MySQL username
        password="1234",    # Your MySQL password
        database="my_database"  # The database you created earlier
    )

    if mydb.is_connected():
        print("✅ Connected to MySQL and using 'my_database'.")

except Error as e:
    print(f"❌ Error connecting to MySQL: {e}")

# Step 3: Create a cursor object
my_cursor = mydb.cursor()

# Step 4: Select and display all records from the 'customers' table
try:
    print("\n📋 All Customer Records:")
    my_cursor.execute("SELECT * FROM customers")
    records = my_cursor.fetchall()

    # Print all records in a readable format
    for row in records:
        # Corrected: Only 3 columns (name, address, email)
        print(f"👤 {row[0]} | 🏠 {row[1]} | ✉️ {row[2]}")

except Error as e:
    print(f"❌ Error retrieving records: {e}")

# Step 5: Select and display specific columns
try:
    print("\n👤 Customer Names:")
    my_cursor.execute("SELECT name FROM customers")
    for (name,) in my_cursor.fetchall():
        print(" -", name)

    print("\n🏠 Customer Addresses:")
    my_cursor.execute("SELECT address FROM customers")
    for (address,) in my_cursor.fetchall():
        print(" -", address)

    print("\n✉️ Customer Emails:")
    my_cursor.execute("SELECT email FROM customers")
    for (email,) in my_cursor.fetchall():
        print(" -", email)

except Error as e:
    print(f"❌ Error retrieving specific columns: {e}")

# Step 6: Close the cursor and connection
my_cursor.close()
mydb.close()
print("\n🔒 Connection closed successfully.")
