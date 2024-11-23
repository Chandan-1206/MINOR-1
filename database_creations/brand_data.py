from pymongo import MongoClient

# Connect to MongoDB (replace <connection_string> with your actual MongoDB connection string if needed)
client = MongoClient("mongodb://localhost:27017/")

# Connect to database and create collection
db = client["clyx"]
brands_collection = db["brands"]

# Sample data
brands_data = [
    {
        "brand_id": "br_1",
        "brand_name": "GreenSpark",
        "industry": "Sustainable and Eco-Friendly Products",
        "contact_person": {
            "name": "Aarav Mehta",
            "email": "aarav.mehta@greenspark.com",
            "phone": "+91-9876543210"
        }
    },
    {
        "brand_id": "br_2",
        "brand_name": "TechNova",
        "industry": "Technology and Software",
        "contact_person": {
            "name": "Priya Sharma",
            "email": "priya.sharma@technova.com",
            "phone": "+91-9123456789"
        }
    },
    {
        "brand_id": "br_3",
        "brand_name": "FitGen",
        "industry": "Health and Wellness",
        "contact_person": {
            "name": "Rohan Gupta",
            "email": "rohan.gupta@fitgen.com",
            "phone": "+91-9988776655"
        }
    },
    {
        "brand_id": "br_4",
        "brand_name": "PlayCore",
        "industry": "Gaming and eSports",
        "contact_person": {
            "name": "Kavya Nair",
            "email": "kavya.nair@playcore.com",
            "phone": "+91-9871234567"
        }
    },
    {
        "brand_id": "br_5",
        "brand_name": "Fashionista Edge",
        "industry": "Fashion and Beauty Tech",
        "contact_person": {
            "name": "Aditya Kapoor",
            "email": "aditya.kapoor@fashionistaedge.com",
            "phone": "+91-9765432100"
        }
    }
]

# Insert data into the collection
result = brands_collection.insert_many(brands_data)

# Output inserted IDs for confirmation
print("sample brands added successfully !!")
