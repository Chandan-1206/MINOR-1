from pymongo import MongoClient
import joblib
import re

# Load the saved model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["influencer_comment_data"]
collection = db["comments_summary"]

# Preprocessing function to clean comments
def preprocess_comment(comment):
    comment = comment.lower()
    comment = re.sub(r"http\S+|www\S+|https\S+", "", comment)
    comment = re.sub(r"\@\w+|\#", "", comment)
    comment = re.sub(r"[^\w\s]", "", comment)
    return comment

# Function to classify comments and update influencer data in MongoDB
def analyze_and_update_comments(influencer_id, comments):
    # Preprocess and classify comments
    cleaned_comments = [preprocess_comment(comment) for comment in comments]
    X = vectorizer.transform(cleaned_comments)
    predictions = model.predict(X)

    # Count positive and negative comments
    new_total_comments = len(comments)
    new_negative_comments = int(sum(predictions))  # Count how many are negative (1 indicates negative)
    new_positive_comments = new_total_comments - new_negative_comments

    # Fetch existing data for influencer
    existing_record = collection.find_one({"influencer_id": influencer_id})

    if existing_record:
        # Update counts by adding new comments
        total_comments = existing_record["total_comments"] + new_total_comments
        positive_comments = existing_record["positive_comments"] + new_positive_comments
        negative_comments = existing_record["negative_comments"] + new_negative_comments
    else:
        # Initialize counts if influencer not found
        total_comments = new_total_comments
        positive_comments = new_positive_comments
        negative_comments = new_negative_comments

    # Calculate new reputation based on positive comment ratio
    positive_ratio = (positive_comments / total_comments) * 100
    if positive_ratio >= 90:
        reputation = 10
    elif positive_ratio >= 80:
        reputation = 9
    elif positive_ratio >= 70:
        reputation = 8
    elif positive_ratio >= 60:
        reputation = 7
    elif positive_ratio >= 50:
        reputation = 6
    elif positive_ratio >= 40:
        reputation = 5
    elif positive_ratio >= 30:
        reputation = 4
    elif positive_ratio >= 20:
        reputation = 3
    elif positive_ratio >= 10:
        reputation = 2
    else:
        reputation = 1

    # Prepare data for MongoDB update
    influencer_data = {
        "influencer_id": influencer_id,
        "total_comments": total_comments,
        "positive_comments": positive_comments,
        "negative_comments": negative_comments,
        "reputation": reputation
    }

    # Update if influencer_id exists, otherwise insert
    collection.update_one(
        {"influencer_id": influencer_id},  # Filter to match by influencer_id
        {"$set": influencer_data},         # Update fields
        upsert=True                        # Insert if not found
    )
    print(f"Data for influencer {influencer_id} updated in MongoDB.")

# Example usage
influencer_id = int(input("Enter influencer ID: "))
comments = input("Enter comments (separated by ','): ").split(',')
analyze_and_update_comments(influencer_id, comments)
