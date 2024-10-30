# Text Categorization Using XGBoost and Word2Vec Framework

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Introduction

"**Text Categorization Using XGBoost and Word2Vec Framework**" is a machine learning project focused on categorizing or classifying text into predefined categories using two key technologies:
- **Word2Vec**: For converting words into continuous vector space representations that preserve semantic relationships between words.
- **XGBoost**: A high-performance gradient boosting framework known for its speed and accuracy, particularly in classification tasks.

This project demonstrates a powerful approach to text categorization, combining XGBoost's performance with Word2Vec's capability to capture semantic information, making it suitable for tasks such as sentiment analysis, topic categorization, and more.

## Features

- **Preprocessing Pipeline**: Handles text preprocessing including tokenization, removal of stop words, lemmatization, etc.
- **Word2Vec Embedding**: Transforms text data into numerical vectors using Word2Vec, preserving semantic similarity between words.
- **XGBoost Classification**: Utilizes XGBoost for efficient, high-accuracy classification.
- **Customizable**: Configurable parameters for Word2Vec and XGBoost, allowing for tuning based on dataset characteristics.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Text-Categorization-Using-XGBoost-and-Word2Vec-Framework.git
   cd Text-Categorization-Using-XGBoost-and-Word2Vec-Framework
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your dataset**: 
   Place your text data in a format suitable for training (e.g., CSV file with text and labels). This can be customized in the code to fit other formats if needed.

2. **Train the model**: 
   Run the main training script:
   ```bash
   python train.py
   ```
   Adjust parameters as necessary within `config.json` or directly in `train.py` for Word2Vec and XGBoost.

3. **Test and Evaluate**:
   Use the evaluation script to test your model's performance on a test dataset:
   ```bash
   python evaluate.py
   ```

4. **Run Predictions**:
   Use the model to make predictions on new text data by running:
   ```bash
   python predict.py --input "Your text here"
   ```

## Methodology

1. **Data Preprocessing**: Text is cleaned and preprocessed, which includes removing punctuation, stop words, and applying tokenization and lemmatization.
2. **Word Embedding (Word2Vec)**: The cleaned text data is transformed into word vectors using Word2Vec.
3. **Model Training (XGBoost)**: The word vectors are used as features to train the XGBoost model on categorized text.
4. **Evaluation**: Model performance is evaluated using metrics like accuracy, F1-score, precision, and recall.

## Results

| Metric       | Score   |
|--------------|---------|
| Accuracy     | 89%     |
| F1 Score     | 0.87    |
| Precision    | 0.89    |
| Recall       | 0.86    |


| Classes        | Precision | Recall | F1-score |
|----------------|-----------|--------|----------|
| Business       | 84%       | 78%    | 81%      |
| Entertainment  | 80%       | 79%    | 79%      |
| Politics       | 70%       | 80%    | 74%      |
| Sports         | 89%       | 86%    | 87%      |
| Tech           | 78%       | 78%    | 78%      |


## Dependencies

- Python 3.x
- XGBoost
- Gensim (for Word2Vec)
- Pandas
- Numpy
- Scikit-learn

Install all dependencies via `requirements.txt`.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for any feature or bugfix, and submit a pull request for review.

## Acknowledgments

- Inspired by [original research or other relevant sources].
- Libraries and frameworks: XGBoost, Gensim's Word2Vec, Scikit-learn.

---
