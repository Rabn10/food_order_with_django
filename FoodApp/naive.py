import pandas as pd
from pathlib import Path
import pickle
import os 
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from joblib import dump, load
from scipy import sparse

#loading the model
def load_model():
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_FILE = os.path.join(BASE_DIR, 'FoodApp/models/MNB.pickle')
    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)
    return model
    # model1=load(MODEL_FILE)
    # return model1

def load_vector():
    BASE_DIR = Path(__file__).resolve().parent.parent
    Vector_FILE = os.path.join(BASE_DIR, 'FoodApp/models/tfidf.pkl')
    with open(Vector_FILE, 'rb') as f:
        vector = pickle.load(f)
    return vector
    # vector1=load(Vector_FILE)
    # return vector1

#main prediction
def prediction(review):
    sentiment={
        1:"postive",
        0:"negative",
    }
    model = load_model()

    if not isinstance(review, list):
        review = [review]

    vectorizer = load_vector()
    review_vectorized = vectorizer.transform(review)    
    print("the result is")
    pred=model.predict(review_vectorized)
    return sentiment[pred[0]]