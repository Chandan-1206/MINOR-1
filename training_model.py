import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
import re

# Load the dataset
data = pd.read_csv("sentiment140.csv", encoding="ISO-8859-1", header=None)

# Rename columns for clarity
data.columns = ["target", "ids", "date", "flag", "user", "text"]

# Convert target values (0=negative, 4=positive)
data["target"] = data["target"].replace(4, 1)  # Now 0 for negative, 1 for positive

# Select only the target and text fields
data = data[["target", "text"]]

# Optional: Drop neutral entries if target includes "2" for neutral
data = data[data["target"] != 2]

# Preprocess the text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # Remove user mentions and hashtags
    text = re.sub(r"\@\w+|\#", "", text)
    # Remove punctuations and numbers
    text = re.sub(r"[^\w\s]", "", text)
    return text

data["text"] = data["text"].apply(preprocess_text)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data["text"], data["target"], test_size=0.2, random_state=42)

# Create the TF-IDF vectorizer and transform the data
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=10000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model and vectorizer
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
