import pymongo

# Step 1: Connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: Select the database
db = client["my_database"]

# Step 3: Select the collection to drop
collection = db["customers"]

# Step 4: Drop (delete) the entire collection
collection.drop()

print("The 'customers' collection has been dropped.")
