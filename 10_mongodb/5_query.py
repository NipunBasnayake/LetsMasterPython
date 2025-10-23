import pymongo

# Step 1: Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: Select the database
db = client["my_database"]

# Step 3: Select the collection
collection = db["customers"]

# Example 1: Exact match query
query_exact = {"address": "Highway 37"}  # Find documents where address is exactly "Highway 37"
result_exact = collection.find(query_exact)

print("Documents with address 'Highway 37':")
for doc in result_exact:
    print(doc)

# Example 2: Comparison query using $gt (greater than)
query_compare = {"name": {"$gt": "John"}}  # Find documents where name > "John"
result_compare = collection.find(query_compare)

print("\nDocuments where name > 'John':")
for doc in result_compare:
    print(doc)

# Example 3: Using projection to include only specific fields
query_proj = {"address": "Highway 37"}  # Query remains the same
projection = {"name": 1, "address": 1, "_id": 0}  # Include only name and address
result_proj = collection.find(query_proj, projection)

print("\nDocuments with projection (only name and address):")
for doc in result_proj:
    print(doc)

# Example 4: Using $regex to find documents with partial match
query_regex = {"name": {"$regex": "^A"}}  # Find names starting with "A"
result_regex = collection.find(query_regex)

print("\nDocuments where name starts with 'A':")
for doc in result_regex:
    print(doc)
