# Step 1: Import the PyMongo library
import pymongo

# Step 2: Connect to the local MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 3: Create or select a database
db = client["my_database"]

# Step 4: Create or select a collection
collection = db["customers"]

# Step 5: Insert one document (record) into the collection
customer_id = collection.insert_one({
    "name": "John",
    "address": "Highway 37"
}).inserted_id

# Step 6: Print the automatically generated unique ID of the inserted document
print("Customer ID:", customer_id)

# Step 7 (Optional): Retrieve and print the inserted document to verify
inserted_doc = collection.find_one({"_id": customer_id})
print("Inserted Document:", inserted_doc)
