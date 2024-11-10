import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib  # for saving the model

# Load preprocessed data
data = pd.read_csv("processed_train.csv")

# Handle missing values in 'cleaned_comment_text'
data['cleaned_comment_text'] = data['cleaned_comment_text'].fillna('')

# Define target variable
data['is_toxic'] = data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].max(axis=1)

# Split data
X = data['cleaned_comment_text']
y = data['is_toxic']

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

# Model training
model = LogisticRegression()
model.fit(X_tfidf, y)

# Save the trained model and vectorizer
joblib.dump(model, 'toxic_comment_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

print("Model and vectorizer saved successfully!")
