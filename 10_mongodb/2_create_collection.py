import pymongo

# Step 1: Connect to the local MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: Access the database
database = client["my_database"]

# Step 3: Access the 'customers' collection
collection = database["customers"]

# Step 4: Print the collection object
print("Collection object:", collection)

# Step 5: List and print all existing collections in the database
existing_collections = database.list_collection_names()
print("Existing collections:", existing_collections)
