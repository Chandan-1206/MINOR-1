# MINOR-1
# project CLYX
# Influencer-Brand Matching Backend

## APIs:
- `/` - Home route
- `/influencers` - Get all influencers
- `/match?engagement=<rate>` - Match influencers by engagement rate
- `/brand_match?audience=<size>` - Match influencers by audience size
- `/add_influencer` - Add new influencer (POST method)

# Troll-Scan
This project preprocesses a dataset of comments, performs text feature extraction, and trains a machine learning model to classify comments as toxic or non-toxic. The workflow includes data preprocessing, feature extraction using TF-IDF, training a logistic regression model, and saving the trained model for later use.

Files Overview
1. processing_data.py
This script preprocesses the raw dataset by:
Loading and cleaning data (removing missing values).
Adding a binary toxicity label based on multiple columns.
Preprocessing text by removing punctuation, tokenizing, and lemmatizing.
Saving the cleaned dataset for model training.

3. model_training.py
This script:
Loads the preprocessed data.
Handles missing values and prepares the dataset for training.
Extracts features from text using TF-IDF vectorization.
Trains a logistic regression model to classify comments as toxic or non-toxic.
Saves the trained model and vectorizer for future use.

3. classify_data.py
This script:
Loads the trained model and TF-IDF vectorizer.
Defines a function to classify new comments as toxic or non-toxic.
Takes user input and predicts whether the comment is toxic based on the pre-trained model.

Key Steps:
Model and Vectorizer Loading: The trained model (toxic_comment_model.pkl) and vectorizer (tfidf_vectorizer.pkl) are loaded.
Prediction: The script uses the model to predict if a new input comment is toxic or non-toxic.
Output: Based on the model's prediction, it outputs either "Toxic Comment" or "Non-Toxic Comment".

Dependencies
joblib
scikit-learn

How to Use
Ensure that the trained model (toxic_comment_model.pkl) and the vectorizer (tfidf_vectorizer.pkl) are available.
Run classify_data.py.
Enter a comment when prompted, and the script will output whether the comment is toxic or non-toxic.
