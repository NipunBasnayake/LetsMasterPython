import pymongo

# Step 1: Connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: Select the database and collection
db = client["my_database"]
collection = db["customers"]

# Example 1: Delete all documents where the name is "John Doe"
delete_query = {"name": "John Doe"}
collection.delete_many(delete_query)
print("Documents with name 'John Doe' have been deleted.")

# Example 2: Delete all documents where age is greater than or equal to 30
delete_many_query = {"age": {"$gte": 30}}
collection.delete_many(delete_many_query)
print("Documents with age greater than or equal to 30 have been deleted.")
