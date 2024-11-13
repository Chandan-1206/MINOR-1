from pymongo import MongoClient
import random

# Connect to MongoDB with a new database name
client = MongoClient("mongodb://localhost:27017/")
db = client["influencer_data"]  # New database name
collection = db["influencers_summary"]

# Sample categories for influencers
categories = ["Fashion", "Tech", "Food", "Travel", "Fitness", "Beauty", "Lifestyle", "Gaming", "Education", "Entertainment"]
regions = ["North America", "Europe", "Asia", "South America", "Africa", "Australia"]

# Function to generate sample data for influencers
def create_sample_influencers(num_influencers=100):
    for i in range(num_influencers):
        influencer_id = i + 1
        username = f"influencer_{influencer_id}"
        age = random.randint(18, 60)
        gender = random.choice(["Male", "Female", "Other"])
        category = random.choice(categories)
        followers = random.randint(1000, 1000000)
        followees = random.randint(100, 5000)
        engagement_rate = round(random.uniform(1, 10), 2)  # engagement rate in percentage

        # Audience data
        audience_age_percentage = {
            "13-17": round(random.uniform(0, 20), 2),
            "18-24": round(random.uniform(10, 30), 2),
            "25-34": round(random.uniform(20, 40), 2),
            "35-44": round(random.uniform(10, 30), 2),
            "45-54": round(random.uniform(0, 20), 2),
            "55+": round(random.uniform(0, 10), 2),
        }
        
        # Adjust percentages to sum to ~100%
        total_percentage = sum(audience_age_percentage.values())
        for key in audience_age_percentage:
            audience_age_percentage[key] = round((audience_age_percentage[key] / total_percentage) * 100, 2)

        # Gender ratio for audience
        male_percentage = round(random.uniform(40, 60), 2)
        female_percentage = round(100 - male_percentage, 2)
        audience_gender_ratio = {
            "Male": male_percentage,
            "Female": female_percentage
        }

        # Regions for audience
        audience_regions = {region: round(random.uniform(0, 100), 2) for region in regions}

        # Create influencer data dictionary
        influencer_data = {
            "influencer_id": influencer_id,
            "username": username,
            "age": age,
            "gender": gender,
            "category": category,
            "followers": followers,
            "followees": followees,
            "engagement_rate": engagement_rate,
            "audience_age_percentage": audience_age_percentage,
            "audience_gender_ratio": audience_gender_ratio,
            "audience_regions": audience_regions
        }

        # Insert the influencer data into the MongoDB collection
        collection.insert_one(influencer_data)

# Generate data for 100 influencers
create_sample_influencers(100)

print("Sample data for influencers created and inserted into MongoDB.")