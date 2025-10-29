# Step 1: Import the MySQL Connector library
import mysql.connector
from mysql.connector import Error

# Step 2: Connect to the MySQL server and select the database
try:
    mydb = mysql.connector.connect(
        host="localhost",    # Your MySQL host (default: localhost)
        user="root",         # Your MySQL username
        password="1234",     # Your MySQL password
        database="my_database"  # The database you created earlier
    )

    if mydb.is_connected():
        print("✅ Successfully connected to MySQL and selected 'my_database'.")

except Error as e:
    print(f"❌ Error connecting to MySQL: {e}")

# Step 3: Create a cursor object
my_cursor = mydb.cursor()

# Step 4: Write an SQL query to insert records into the table
insert_query = """
INSERT INTO customers (name, address, email)
VALUES (%s, %s, %s)
"""

# Step 5: Prepare multiple records to insert
customers_data = [
    ("Amal Perera", "Colombo", "amal@example.com"),
    ("Kamal Silva", "Kandy", "kamal@example.com"),
    ("Nimal Fernando", "Galle", "nimal@example.com"),
]

# Step 6: Execute the query and commit the changes
try:
    my_cursor.executemany(insert_query, customers_data)
    mydb.commit()  # Important! Saves the changes to the database
    print(f"✅ {my_cursor.rowcount} records inserted successfully into 'customers' table.")

except Error as e:
    print(f"❌ Error inserting data: {e}")
    mydb.rollback()  # Undo changes if an error occurs

# Step 7: Verify the inserted data
print("\n📋 Current Records in 'customers':")
my_cursor.execute("SELECT * FROM customers")
for record in my_cursor.fetchall():
    print(record)

# Step 8: Close the cursor and database connection
my_cursor.close()
mydb.close()
print("\n🔒 Connection closed successfully.")
