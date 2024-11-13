from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load the saved model and vectorizer
model = joblib.load('sentiment_model.pkl')  # Load your trained model
vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Load your trained vectorizer

# Function to classify comments as positive or negative
def classify_comments(comments):
    # Preprocess comments (e.g., lowercase)
    cleaned_comments = [comment.lower() for comment in comments]

    # Convert comments to feature vectors using the loaded vectorizer
    X = vectorizer.transform(cleaned_comments)

    # Predict sentiment for each comment
    predictions = model.predict(X)

    # Convert predictions to 'positive' or 'negative' labels
    results = ["positive" if pred == 1 else "negative" for pred in predictions]

    # Print results
    for comment, sentiment in zip(comments, results):
        print(f"Comment: \"{comment}\" => Sentiment: {sentiment}")

# Example usage
comments = [
    "I absolutely love this!",
    "This is terrible.",
    "Such a great experience.",
    "Worst service ever.",
    "I'm very happy with the results.",
    "This is disappointing."
]

classify_comments(comments)
