import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["customers"]

# Example 1: Exact match query
query_exact = {"address": "Highway 37"}
result_exact = collection.find(query_exact)

print("Documents with address 'Highway 37':")
for doc in result_exact:
    print(doc)

# Example 2: Comparison query using $gt (greater than)
query_compare = {"name": {"$gt": "John"}}
result_compare = collection.find(query_compare)

print("\nDocuments where name > 'John':")
for doc in result_compare:
    print(doc)
