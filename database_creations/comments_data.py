from pymongo import MongoClient
import random

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["clyx"]
# Create a collection
toxicity_col = db["comments_data"]

# Function to calculate rating based on positive comment percentage
def calculate_rating(positive_comments, total_comments):
    positive_ratio = (positive_comments / total_comments) * 100
    
    if positive_ratio >= 90:
        return round(random.uniform(9.0, 10.0), 1)
    elif positive_ratio >= 80:
        return round(random.uniform(8.0, 8.9), 1)
    elif positive_ratio >= 70:
        return round(random.uniform(7.0, 7.9), 1)
    elif positive_ratio >= 60:
        return round(random.uniform(6.0, 6.9), 1)
    elif positive_ratio >= 50:
        return round(random.uniform(5.0, 5.9), 1)
    elif positive_ratio >= 40:
        return round(random.uniform(4.0, 4.9), 1)
    elif positive_ratio >= 30:
        return round(random.uniform(3.0, 3.9), 1)
    elif positive_ratio >= 20:
        return round(random.uniform(2.0, 2.9), 1)
    elif positive_ratio >= 10:
        return round(random.uniform(1.0, 1.9), 1)
    else:
        return 1.0

# Reference the Influencers collection
influencers_col = db["influencers"]
influencers = influencers_col.find({}, {"Influencer_Id": 1})  # Fetch all influencer IDs

# Generate and insert toxicity data
toxicity_data = []
for influencer in influencers:
    influencer_id = influencer["Influencer_Id"]
    total_comments = random.randint(500, 5000)  # Total comments
    positive_comments = random.randint(0, total_comments)  # Positive (non-toxic) comments
    negative_comments = total_comments - positive_comments  # Toxic comments
    
    # Calculate the rating based on positive comments
    rating = calculate_rating(positive_comments, total_comments)
    
    # Create a document for the comments_data collection
    toxicity_record = {
        "Influencer_Id": influencer_id,
        "Total_Comments": total_comments,
        "Positive_Comments": positive_comments,
        "Negative_Comments": negative_comments,
        "Rating": rating
    }
    toxicity_data.append(toxicity_record)

# Insert the generated data into the comments_data collection
toxicity_col.insert_many(toxicity_data)
print("Toxicity data generated and stored in 'comments_data' collection.")

# Update the ratings in the Influencers collection
for record in toxicity_data:
    influencers_col.update_one(
        {"Influencer_Id": record["Influencer_Id"]},
        {"$set": {"Rating": record["Rating"]}}
    )

print("Ratings updated in 'influencers' collection.")
