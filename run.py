import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('dataset.csv')

import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

import re

def clean_feature_vector(vector_str):
    # Use regex to add commas between numbers
    vector_str = re.sub(r'(?<=\d)\s+(?=-?\d)', ', ', vector_str)
    return np.array(eval(vector_str))

# Clean and convert feature vectors to numpy arrays
X = np.array([clean_feature_vector(v) for v in df['feature_vector']])

# Encode labels to numeric values
label_encoder = LabelEncoder()
y = df['label']
y_encoded = label_encoder.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train XGBoost classifier
xgb_clf = xgb.XGBClassifier(objective='multi:softmax', num_class=len(label_encoder.classes_), eval_metric='mlogloss', use_label_encoder=False)
xgb_clf.fit(X_train, y_train)


y_pred = xgb_clf.predict(X_test)

# Evaluate the classifier
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))


import numpy as np
import gensim
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained Word2Vec model
word2vec_model_path = 'word2vec_model.model'  # Update with the actual path
word2vec = gensim.models.Word2Vec.load(word2vec_model_path)

# Function to convert text into a feature vector using Word2Vec
def text_to_feature_vector(text):
    words = text.split()  # Simple tokenization, you may use a better tokenizer
    word_vectors = []

    for word in words:
        if word in word2vec.wv:  # Check if the word exists in the Word2Vec vocabulary
            word_vectors.append(word2vec.wv[word])
    
    if len(word_vectors) > 0:
        # Return the average of word vectors for all words in the text
        return np.mean(word_vectors, axis=0)
    else:
        # If none of the words are in the Word2Vec model, return a zero vector
        return np.zeros(word2vec.vector_size)

# Function to predict the label for user-entered text
def predict_label(user_text):
    # Convert user-entered text to a feature vector using Word2Vec
    feature_vector = text_to_feature_vector(user_text)

    # Reshape feature_vector for prediction (1 sample with feature_vector length)
    feature_vector = feature_vector.reshape(1, -1)

    # Make prediction using the trained XGBoost classifier
    predicted_label_index = xgb_clf.predict(feature_vector)[0]

    # Get the actual label name from the encoded label
    predicted_label = label_encoder.inverse_transform([predicted_label_index])[0]

    return predicted_label

# Example usage
#user_text = input("Enter some text: ")
# predicted_label = predict_label(user_text)
# print(f"The predicted label is: {predicted_label}")

