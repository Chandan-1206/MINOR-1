from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
credentials_db = client['clyx']  # Access the database

# Collections
influencer_credentials_collection = credentials_db['influencer_credentials']
influencers_collection = credentials_db['influencers']  # Existing influencers collection

def create_credentials_from_influencers():
    """Generate influencer credentials by fetching emails from the influencers collection."""
    influencers = influencers_collection.find().limit(90)  # Fetch only the first 90 influencers

    for influencer in influencers:
        user_id = influencer.get("Influencer_Id")
        email = influencer.get("E-mail")
        
        if user_id and email:  # Ensure both fields are present
            password = f"password_{user_id}"  # Generate a sample password
            new_credentials = {
                "user_id": user_id,
                "email": email,
                "password": password  # Store plain password for testing
            }
            influencer_credentials_collection.insert_one(new_credentials)
            print(f"Influencer credentials created: {new_credentials}")
        else:
            print(f"Skipping influencer with missing data: {influencer}")

def main():
    create_credentials_from_influencers()

if __name__ == "__main__":
    main()
