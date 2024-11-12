from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['influencer_database']  # Database name

# Sample influencer data
sample_influencers = [
    {"name": "Alice Smith", "audience": 25000, "engagement_rate": 6.0},
    {"name": "Bob Johnson", "audience": 30000, "engagement_rate": 7.5},
    {"name": "Charlie Brown", "audience": 5000, "engagement_rate": 4.0},
    {"name": "Diana Prince", "audience": 15000, "engagement_rate": 5.0},
    {"name": "Elon Musk", "audience": 500000, "engagement_rate": 10.0},
    {"name": "Jane Doe", "audience": 10000, "engagement_rate": 3.5},
    {"name": "Mark Zuckerberg", "audience": 200000, "engagement_rate": 8.0},
    {"name": "Taylor Swift", "audience": 300000, "engagement_rate": 9.0},
    {"name": "Cristiano Ronaldo", "audience": 400000, "engagement_rate": 11.0},
    {"name": "Kylie Jenner", "audience": 350000, "engagement_rate": 12.0}
]

# Insert sample data into the influencers collection
result = db['influencers'].insert_many(sample_influencers)

print(f"Inserted {len(result.inserted_ids)} sample influencers into the database.")
