import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["customers"]

# Example 1: Limit to first 5 documents
result1 = collection.find().limit(5)
print("First 5 documents:")
for doc in result1:
    print(doc)

# Example 2: Skip first 2 documents, then limit next 5
result2 = collection.find().skip(2).limit(5)
print("\nDocuments after skipping 2:")
for doc in result2:
    print(doc)

# Example 3: Pagination using skip and limit
page_number = 3
page_size = 5
result3 = collection.find().skip((page_number - 1) * page_size).limit(page_size)
print(f"\nDocuments on page {page_number}:")
for doc in result3:
    print(doc)

# Example 4: User-defined limit
user_limit = int(input("\nEnter the number of documents to retrieve: "))
result4 = collection.find().limit(user_limit)
print(f"\nFirst {user_limit} documents:")
for doc in result4:
    print(doc)
