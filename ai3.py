# --- SIMPLIFIED CYBERBULLYING DETECTOR (Avoids Pandas) ---
# NOTE: Still requires scikit-learn and nltk to be installed via pip.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
import random

# --- 1. Internal Dataset Creation ---

# Data is stored in simple Python lists (no pandas needed)
X_text = [
    "You are so useless, just delete your account.",             # Bullying (1)
    "Your work is garbage, absolute waste of time.",           # Bullying (1)
    "Nobody likes you, honestly, just quit.",                   # Bullying (1)
    "That post was really funny, great job!",                  # Not Bullying (0)
    "Thanks for the help, I appreciate your advice.",          # Not Bullying (0)
    "What a beautiful day to be outside and enjoy the sun.",    # Not Bullying (0)
    "You look terrible today. Did you even try?",              # Bullying (1)
    "I love this new song, it's my favorite."                   # Not Bullying (0)
]
y_labels = np.array([1, 1, 1, 0, 0, 0, 1, 0]) # Target labels (1=Bullying, 0=Not)

# --- 2. Feature Extraction and Training ---

print("1. Initializing TF-IDF Vectorizer...")
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))

# Fit the vectorizer and transform the text data
X_vectorized = vectorizer.fit_transform(X_text)

# Initialize and Train the Model (Using ALL data for simplicity, since no testing is done here)
print("2. Training Logistic Regression Model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_vectorized, y_labels)
print("3. Training Complete.")

# --- 3. Real-Time Prediction Function ---

def predict_cyberbullying(comment, model, vectorizer):
    """Takes a new comment and returns its classification and confidence."""
    
    # Vectorize the new comment
    new_comment_vectorized = vectorizer.transform([comment])
    
    # Predict the class (0 or 1)
    prediction = model.predict(new_comment_vectorized)[0]
    
    # Get the confidence
    probabilities = model.predict_proba(new_comment_vectorized)[0]
    confidence = probabilities[prediction]
    
    # Map the numerical prediction back to a human-readable label
    label = "🔥 CYBERBULLYING DETECTED" if prediction == 1 else "✅ NOT CYBERBULLYING"
    
    return label, confidence

# --- 4. Test the Model with New Data ---

print("\n\n--- 🤖 AI Cyberbullying Detector Live Test ---")

test_comments = [
    "You are the worst person I have ever met, go away.",
    "This is a fantastic feature, thank you for sharing!",
    "I hope you fail at everything you try to do.",
    "Just ignore the trolls, don't feed them."
]

for comment in test_comments:
    result, confidence = predict_cyberbullying(comment, model, vectorizer)
    
    # Display the result
    print(f"\n[INPUT]: '{comment}'")
    print(f"  [PREDICTION]: {result}")
    print(f"  [CONFIDENCE]: {confidence:.4f}")
    
print("\n-------------------------------------------")
print("Detection system is operational and ready for deployment.")
