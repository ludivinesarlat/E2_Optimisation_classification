# Dependencies
from flask import Flask,render_template, request, jsonify
import traceback
import pandas as pd
import numpy as np
import sklearn
import sys
import pickle
from models import nettoyage, trouve_journal
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def envoi():
    return  render_template("page.html")
     
@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            #json_2 = json_[0]["titre"]
            mon_article = request.form['monArticle']
            article = nettoyage(mon_article)
            query = tfidf_.transform([article])
            prediction = trouve_journal(lr.predict(query))
            probas = lr.predict_proba(query)[0]
            proba = [round(x,4) for x in probas]
            return  render_template("result.html", name=prediction, a_traduire=mon_article, probas=proba)
            # return jsonify({'prediction': prediction})

        except Exception as e:
            print("Une erreur s'est produite")
            return render_template("page.html")
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    with open("./src/models_pickle/file_model_fitted_Knn.pkl", 'rb') as file_model:
        lr = pickle.load(file_model)  
        print ('Model loaded')

    with open("./src/models_pickle/file_tfidf.pkl", 'rb') as tfidf:
        tfidf_ = pickle.load(tfidf)
        print ('tfidf transfo loaded')

    app.run(port=12345, debug=True)
   