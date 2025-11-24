# from flask import Flask, render_template, request, redirect, url_for
# import numpy as np
# import gensim
# from sklearn.preprocessing import LabelEncoder
# import xgboost as xgb
# import pandas as pd

# # Load the pre-trained Word2Vec model and trained XGBoost classifier
# word2vec_model_path = 'word2vec_model.model'  # Update with actual path
# word2vec = gensim.models.Word2Vec.load(word2vec_model_path)

# # Load label encoder and trained XGBoost classifier
# df = pd.read_csv('dataset.csv')
# label_encoder = LabelEncoder()
# y = df['label']
# y_encoded = label_encoder.fit_transform(y)

# xgb_clf = xgb.XGBClassifier(objective='multi:softmax', num_class=len(label_encoder.classes_), eval_metric='mlogloss', use_label_encoder=False)
# X = np.array([np.random.rand(300) for _ in df['feature_vector']])  # Dummy vector for re-training
# xgb_clf.fit(X, y_encoded)

# # Flask app setup
# app = Flask(__name__)

# # Function to convert text into a feature vector using Word2Vec
# def text_to_feature_vector(text):
#     words = text.split()  # Simple tokenization
#     word_vectors = []

#     for word in words:
#         if word in word2vec.wv:  # Check if the word exists in Word2Vec vocabulary
#             word_vectors.append(word2vec.wv[word])

#     if len(word_vectors) > 0:
#         # Return the average of word vectors for all words in the text
#         return np.mean(word_vectors, axis=0)
#     else:
#         # Return zero vector if none of the words are found in Word2Vec
#         return np.zeros(word2vec.vector_size)

# # Route for the input page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route for processing and displaying the result
# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         user_text = request.form['text']  # Get text from form

#         # Convert text to feature vector using Word2Vec
#         feature_vector = text_to_feature_vector(user_text)
#         feature_vector = feature_vector.reshape(1, -1)

#         # Predict the label using the trained XGBoost classifier
#         predicted_label_index = xgb_clf.predict(feature_vector)[0]
#         predicted_label = label_encoder.inverse_transform([predicted_label_index])[0]

#         return render_template('result.html', label=predicted_label)

# if __name__ == '__main__':
#     app.run(debug=True)
import streamlit as st
from run import predict_label

st.title("Text Categorization ")

st.write("This is a text categorization model using XGBOOST Model ")
prompt=st.text_area("Enter the text")
#st.write(prompt)


if st.button('submit')==True:
    response = predict_label(prompt)

    st.write(response)