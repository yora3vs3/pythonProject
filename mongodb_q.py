from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import DuplicateKeyError, ServerSelectionTimeoutError
from datetime import datetime
from bson.objectid import ObjectId
import pprint
from pymongo import InsertOne, DeleteOne, UpdateOne
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)  # 5 second timeout
    db = client['complex_db']
    collection = db['example_collection']
except ServerSelectionTimeoutError as err:
    logging.error("Failed to connect to MongoDB: %s", err)
    exit(1)

# Drop collection if exists to start fresh
try:
    collection.drop()
except Exception as e:
    logging.error("Failed to drop collection: %s", e)

# Insert multiple documents with complex structures
data = [
    {
        "_id": 1,
        "name": "Alice",
        "age": 29,
        "scores": {"math": 85, "english": 92},
        "registered_at": datetime(2022, 5, 17),
        "is_active": True,
        "friends": [ObjectId(), ObjectId(), ObjectId()],
        "location": {"type": "Point", "coordinates": [-73.97, 40.77]},
        "tags": ["student", "math-club"]
    },
    {
        "_id": 2,
        "name": "Bob",
        "age": 32,
        "scores": {"math": 78, "english": 85},
        "registered_at": datetime(2023, 3, 10),
        "is_active": False,
        "friends": [ObjectId(), ObjectId()],
        "location": {"type": "Point", "coordinates": [-74.00, 40.71]},
        "tags": ["alumni", "developer"]
    },
    {
        "_id": 3,
        "name": "Charlie",
        "age": 25,
        "scores": {"math": 90, "english": 88},
        "registered_at": datetime(2022, 7, 25),
        "is_active": True,
        "friends": [ObjectId()],
        "location": {"type": "Point", "coordinates": [-73.98, 40.75]},
        "tags": ["student", "chess-club"]
    }
]

try:
    collection.insert_many(data, ordered=False)
    logging.info("Documents inserted successfully!")
except DuplicateKeyError as e:
    logging.warning("Duplicate Key Error: %s", e)

# Create complex indexes for faster querying
try:
    collection.create_index([("name", ASCENDING), ("age", DESCENDING)], unique=True)
    collection.create_index([("location", "2dsphere")])  # For geospatial queries
    collection.create_index("tags")  # Multikey index for array field
except Exception as e:
    logging.error("Failed to create index: %s", e)

# Query examples
logging.info("\n=== Querying Documents ===")

try:
    # Find documents with a filter, projection, and sorting
    docs = collection.find(
        {"is_active": True},
        {"_id": 0, "name": 1, "age": 1, "tags": 1}
    ).sort("age", DESCENDING)
    logging.info("\nActive users sorted by age:")
    for doc in docs:
        pprint.pprint(doc)
except Exception as e:
    logging.error("Failed to query documents: %s", e)

# Aggregation pipeline example
logging.info("\n=== Aggregation Pipeline ===")
pipeline = [
    {"$match": {"is_active": True}},
    {"$group": {
        "_id": "$tags",
        "average_age": {"$avg": "$age"},
        "total_users": {"$sum": 1}
    }},
    {"$sort": {"average_age": -1}}
]

try:
    agg_results = collection.aggregate(pipeline)
    for result in agg_results:
        pprint.pprint(result)
except Exception as e:
    logging.error("Failed to aggregate documents: %s", e)

# Update document example
logging.info("\n=== Updating Documents ===")
try:
    update_result = collection.update_one(
        {"name": "Alice"},
        {"$set": {"is_active": False, "last_modified": datetime.now()}}
    )
    logging.info("Matched: %d, Modified: %d", update_result.matched_count, update_result.modified_count)
except Exception as e:
    logging.error("Failed to update documents: %s", e)

# Delete documents example
logging.info("\n=== Deleting Documents ===")
try:
    delete_result = collection.delete_many({"is_active": False})
    logging.info("Deleted documents count: %d", delete_result.deleted_count)
except Exception as e:
    logging.error("Failed to delete documents: %s", e)

# Geospatial query example
logging.info("\n=== Geospatial Query ===")
try:
    geospatial_results = collection.find({
        "location": {
            "$near": {
                "$geometry": {"type": "Point", "coordinates": [-74.0, 40.72]},
                "$maxDistance": 5000  # 5 km radius
            }
        }
    })
    logging.info("Documents near location (-74.0, 40.72):")
    for doc in geospatial_results:
        pprint.pprint(doc)
except Exception as e:
    logging.error("Failed to perform geospatial query: %s", e)

# Bulk write operation example
bulk_operations = [
    InsertOne({
        "_id": 4,
        "name": "Diana",
        "age": 28,
        "scores": {"math": 95, "english": 91},
        "registered_at": datetime(2023, 2, 5),
        "is_active": True,
        "tags": ["science-club", "developer"]
    }),
    UpdateOne({"name": "Charlie"}, {"$set": {"age": 26}}),
    DeleteOne({"name": "Bob"})
]
try:
    bulk_result = collection.bulk_write(bulk_operations)
    logging.info("\nBulk Operation Results:")
    logging.info("Inserted: %d", bulk_result.inserted_count)
    logging.info("Updated: %d", bulk_result.modified_count)
    logging.info("Deleted: %d", bulk_result.deleted_count)
except Exception as e:
    logging.error("Failed to perform bulk operations: %s", e)

# Closing connection
client.close()
