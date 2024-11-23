from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
credentials_db = client['clyx']  # Access the database

# Collections
brand_credentials_collection = credentials_db['brand_credentials']
brands_collection = credentials_db['brands']  # Existing brands collection

def create_credentials_from_brands():
    """Generate brand credentials by fetching data from the brands collection."""
    brands = brands_collection.find()  # Fetch all documents from the brands collection

    for brand in brands:
        user_id = brand.get("brand_id")
        contact_person = brand.get("contact_person", {})
        email = contact_person.get("email")
        
        if user_id and email:  # Ensure both user_id and email are present
            password = f"password_{user_id}"  # Generate a sample password
            new_credentials = {
                "user_id": user_id,
                "email": email,
                "password": password  # Store plain password for testing
            }
            brand_credentials_collection.insert_one(new_credentials)
            print(f"Brand credentials created: {new_credentials}")
        else:
            print(f"Skipping brand with missing data: {brand}")

def main():
    create_credentials_from_brands()

if __name__ == "__main__":
    main()
