from pymongo import MongoClient
import random

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["clyx"]

# Collection for influencers
influencers_col = db["influencers"]

# Random Data Generators
def generate_name():
    first_names = ["Aarav", "Vivaan", "Anaya", "Ishita", "Kabir", "Meera", "Arjun", "Priya", "Kunal", "Sneha"]
    last_names = ["Sharma", "Verma", "Gupta", "Nair", "Menon", "Patel", "Kumar", "Reddy", "Das", "Bose"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_email(name):
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    return f"{name.replace(' ', '').lower()}@{random.choice(domains)}"

def generate_random_audience_demographics():
    """
    Randomly assign audience percentages across categories such that the sum equals 100.
    Each influencer can have a different dominant audience category.
    """
    categories = ["Teens", "Youngsters", "Adults", "Middle_Aged", "Senior_Citizens"]
    percentages = [random.randint(5, 50) for _ in categories]  # Generate random numbers for all categories
    total = sum(percentages)
    normalized_percentages = {category: round((value / total) * 100, 2) for category, value in zip(categories, percentages)}
    return normalized_percentages

def generate_audience_gender_ratio():
    male_percentage = round(random.uniform(40, 60), 2)
    female_percentage = round(100 - male_percentage, 2)
    return {"Male": male_percentage, "Female": female_percentage}

def generate_niche():
    niches = [
        "E-commerce and Online Retail", "Technology and Software", "Health and Wellness",
        "Sustainable and Eco-Friendly Products", "Fashion and Beauty Tech", "FinTech",
        "Gaming and eSports", "Streaming and Digital Media", "Electric Vehicles and Clean Energy",
        "Food Tech", "EdTech", "AR/VR and Metaverse", "Digital Content Creation and Influencer Platforms",
        "D2C Lifestyle Brands", "Pet Tech and Premium Pet Products", "Space Tech and Aerospace Innovations",
        "Travel Tech and Experiences", "AI and Data Analytics Solutions", "Luxury Tech", "Mobility Solutions"
    ]
    return random.choice(niches)

# Insert Influencers Data
influencers_data = []
for i in range(1, 101):  # Insert only 1 sample for now
    name = generate_name()
    influencer = {
        "Influencer_Id": f"Inf_{i}",
        "Name": name,
        "Age": random.randint(18, 50),
        "Gender": random.choice(["Male", "Female"]),
        "E-mail": generate_email(name),
        "Insta_ID": f"@{name.replace(' ', '').lower()}",
        "Followers": random.randint(10000, 1000000),
        "Followees": random.randint(500, 5000),
        "Engagement_Rate": round(random.uniform(1.0, 10.0), 2),  # Engagement rate in percentage
        "Audience_Demographic_Percentage": generate_random_audience_demographics(),
        "Audience_Gender_Ratio": generate_audience_gender_ratio(),
        "Niche": generate_niche(),
        "Rating": -1  # Initialize ratings to -1
    }
    influencers_data.append(influencer)

# Insert data into the collection
influencers_col.insert_many(influencers_data)

print("Sample influencer added !")
