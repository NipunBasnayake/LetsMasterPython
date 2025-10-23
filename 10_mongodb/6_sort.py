import pymongo

# Step 1: Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Step 2: Select the database and collection
db = client["my_database"]
collection = db["customers"]

# Example 1: Sort by 'name' in ascending order (A → Z)
sort_order_asc = [("name", pymongo.ASCENDING)]
result_asc = collection.find().sort(sort_order_asc)

print("Sorted by name (ascending):")
for doc in result_asc:
    print(doc)

# Example 2: Sort by 'name' in descending order (Z → A)
sort_order_desc = [("name", pymongo.DESCENDING)]
result_desc = collection.find().sort(sort_order_desc)

print("\nSorted by name (descending):")
for doc in result_desc:
    print(doc)

# Example 3: Sort by multiple fields — first by 'address' ascending, then by 'name' descending
multi_sort_order = [("address", pymongo.ASCENDING), ("name", pymongo.DESCENDING)]
result_multi = collection.find().sort(multi_sort_order)

print("\nSorted by address (A → Z) and then by name (Z → A):")
for doc in result_multi:
    print(doc)
