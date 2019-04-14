from flask import Flask, render_template, url_for, request
import pickle
import sys
import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        nb_model = open('models/nb_model.pkl','rb')
        nb_clf = joblib.load(nb_model)
        tfidf_vec = open('models/tfidf_vec.pkl', 'rb')
        tfidf = joblib.load(tfidf_vec)
    except IOError:
        print("Could not read pkl files")
        sys.exit()

    
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        data_vec = tfidf.transform(data).toarray()
        predicted_class = int(nb_clf.predict(data_vec))
        #TODO: fix input data so that classes are int's, not floats

        #convert np array to list, use proper indexing to unnest and get correct prob
        predicted_probs = nb_clf.predict_proba(data_vec).tolist()
        pred_prob = round(predicted_probs[0][predicted_class-1], 2)
    
    return render_template('result.html',
                            message=message,
                            prediction = predicted_class,
                            pred_prob = pred_prob)

if __name__ == '__main__':
    app.run(debug=True)
