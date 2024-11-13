from pymongo import MongoClient
import random

# Connect to MongoDB with a new database name
client = MongoClient("mongodb://localhost:27017/")
db = client["influencer_comment_data"]  # New database name
collection = db["comments_summary"]

# Function to calculate reputation based on positive comment percentage
def calculate_reputation(positive_comments, total_comments):
    positive_ratio = (positive_comments / total_comments) * 100
    if positive_ratio >= 90:
        return 10
    elif positive_ratio >= 80:
        return 9
    elif positive_ratio >= 70:
        return 8
    elif positive_ratio >= 60:
        return 7
    elif positive_ratio >= 50:
        return 6
    elif positive_ratio >= 40:
        return 5
    elif positive_ratio >= 30:
        return 4
    elif positive_ratio >= 20:
        return 3
    elif positive_ratio >= 10:
        return 2
    else:
        return 1

# Function to generate sample data for influencers
def create_sample_influencers(num_influencers=100):
    for i in range(num_influencers):
        influencer_id = i + 1
        total_comments = random.randint(500, 10000)
        
        # Generate random number of positive and negative comments
        positive_comments = random.randint(int(total_comments * 0.2), total_comments)
        negative_comments = total_comments - positive_comments
        
        # Calculate reputation based on positive comment percentage
        reputation = calculate_reputation(positive_comments, total_comments)

        influencer_data = {
            "influencer_id": influencer_id,
            "total_comments": total_comments,
            "positive_comments": positive_comments,
            "negative_comments": negative_comments,
            "reputation": reputation
        }

        # Insert the influencer data into the MongoDB collection
        collection.insert_one(influencer_data)

# Generate data for 100 influencers
create_sample_influencers(100)

print("Sample data for influencers created and inserted into MongoDB.")
