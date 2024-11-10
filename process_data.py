import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load necessary NLTK resources
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')

# Load the dataset
data = pd.read_csv("train.csv")

# Drop missing values if any
data = data.dropna()

# Add a new binary column 'is_toxic' where 1 indicates any form of toxicity and 0 means no toxicity
data['is_toxic'] = data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].sum(axis=1) > 0
data['is_toxic'] = data['is_toxic'].astype(int)

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    # Join tokens back into a single string
    return " ".join(tokens)

# Apply preprocessing to the comment_text column
data['cleaned_comment_text'] = data['comment_text'].apply(preprocess_text)

# Save the cleaned dataset to a new CSV file (optional)
data.to_csv("processed_train.csv", index=False)

print("Data preprocessing complete and saved to 'processed_train.csv'")
