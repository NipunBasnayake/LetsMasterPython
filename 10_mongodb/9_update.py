import pymongo

# Step 1: Connect to the local MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: Select the database
db = client["my_database"]

# Step 3: Select the collection
collection = db["customers"]

# Step 4: Define the filter to find document(s)
filter_query = {"name": "John Doe"}  # Find documents where name is 'John Doe'

# Step 5: Define the update operation
update_query = {"$set": {"address": "New Address 123"}}  # Update address field

# Step 6: Update one document (or insert if not found)
result_one = collection.update_one(filter_query, update_query, upsert=True)
print(result_one.modified_count, "document updated (or inserted if not found).")

# Step 7: Update all matching documents
result_many = collection.update_many(filter_query, update_query)
print(result_many.modified_count, "documents updated.")
