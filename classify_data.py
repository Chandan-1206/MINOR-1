import joblib  # for loading the model

# Load the trained model and vectorizer
model = joblib.load('toxic_comment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to predict if a new comment is toxic or not
def predict_toxicity(comment):
    # Preprocess and vectorize the input comment
    comment_tfidf = vectorizer.transform([comment])
    
    # Make prediction (0 for non-toxic, 1 for toxic)
    prediction = model.predict(comment_tfidf)[0]
    
    # Output result
    if prediction == 1:
        return "Toxic Comment"
    else:
        return "Non-Toxic Comment"

# Example usage
new_comment = input("Enter a comment: ")
result = predict_toxicity(new_comment)
print(result)
