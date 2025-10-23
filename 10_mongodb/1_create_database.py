import pymongo

# Step 1: Connect to the local MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: List all existing databases
existing_db = client.list_database_names()
print("Existing databases:", existing_db)

# Step 3: Check if 'my_database' exists, otherwise create a new one
if "my_database" not in existing_db:
    db = client["my_database"]  # Create (reference) the new database

    # Step 4: MongoDB only creates a database after inserting data
    collection = db["customers"]  # Create a collection
    sample_data = {"name": "Amal Perera", "address": "Colombo"}
    collection.insert_one(sample_data)

    print("Database and 'customers' collection created successfully.")
else:
    print("Database already exists.")
