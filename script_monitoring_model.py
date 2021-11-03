import pandas as pd
import pymysql
from sklearn.metrics import precision_score , recall_score, f1_score , accuracy_score
import pickle
import mlflow.sklearn
from Flask_journaux.src.models import nettoyage, encode_journal 
import smtplib

with open("Flask_journaux/src/models_pickle/file_model_fitted_svm_opti.pkl", 'rb') as file_model:
    lr = pickle.load(file_model)  
    print ('Model loaded')


with open("Flask_journaux/src/models_pickle/file_tfidf.pkl", 'rb') as vector:
    tfidf = pickle.load(vector)
    print ('tfidf transfo loaded')
    
connection = pymysql.connect(host='localhost',
                         user='root',
                         password='Ludi24',
                         db='journaux')

# create cursor
cursor = connection.cursor()
# chargement de nouvelles données
query_read = "SELECT * FROM articles where date('2021-04-20')<jour_publication and jour_publication<=date('2021-05-10')"
cursor.execute(query_read)
raw_enregistrement = cursor.fetchall()
connection.commit()
df_test = pd.DataFrame(raw_enregistrement, columns =["id_article", "titre","jour_publication", "categorie","journal"])
cursor.close()
connection.close()

# preprocessing
X2 = df_test.titre.map(lambda x: nettoyage(x))
y2 = df_test.journal.map(lambda x: encode_journal(x))
X2_features = tfidf.transform(X2)

# calcul prediction avec le modèle chargé
pred2 = lr.predict(X2_features)
acc = accuracy_score(y2, pred2)
print('Accurancy', acc)
print('Precision', precision_score(y2, pred2 ,average='weighted'))
print('Recall', recall_score(y2, pred2,average='weighted'))
print('f1-score', f1_score(y2, pred2,average='weighted'))

with mlflow.start_run():
    print("Monitoring Model..")
    mlflow.sklearn.log_model(lr,'SVM')
    mlflow.log_param('algorithm','SVM deployed')
    mlflow.log_param('best_params',lr.get_params(deep=True))
    mlflow.log_metric("score",acc)
    print("Fin de traitement")

if acc < 0.70:
    #email properties
    gmail_user = 'mariebolin@gmail.com'
    gmail_password ='mot2passeG'
    sent_from = 'mariebolin@gmail.com'
    to = ["ludivinesarlat@gmail.com","ludivinesarlat@hotmail.com"]
    subject = 'Alert for model performance'
    email_text = """ The model performance is less than 0.70. Check it    """
    #email send request
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        print ('Email sent!')
        
    except Exception as e:
        print(e)
        print ('Something went wrong...')
    server.quit()