import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["customers"]

# Step 1: Create a query to find documents where address is "Highway 37"
query = {"address": "Highway 37"}

# Step 2: Execute the query
result = collection.find(query)

# Step 3: Iterate over the cursor to print matching documents
print("Matching documents:")
for doc in result:
    print(doc)
