import nltk
import pandas as pd
import contractions
import numpy as np
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


nltk.download("wordnet")

def ignore_symbols(message):
    return "".join(i for i in message if i.isalnum() or i.isspace() or i=="$")
#data cleaning
df = pd.read_csv("spam.csv", encoding="latin-1")
df = df.rename(columns={"v1": "target", "v2": "message"})
df["target"] = df["target"].map({"ham":0,"spam":1})
df = df.dropna(subset=["target"])
df["message"]=df["message"].astype(str).str.lower()
df=df[["target","message"]]
df=df.drop_duplicates(keep="first")
#df=df.to_csv("spam.csv", index="False")



#data preprocessing
df["message"]=df["message"].apply(lambda x: contractions.fix(x))#don't==do not
df["message"] = df["message"].apply(ignore_symbols)
df["message"]=df["message"].str.split()#no need of tokenization now both work same
lem = WordNetLemmatizer()#cut grammers like care==caring, eat==ate==eaten
df["message"]=df["message"].apply(lambda x: [lem.lemmatize(i) for i in x])
df["message"]=df["message"].apply(lambda x:" ".join(x))
#TF-IDF (Term Frequency-Inverse Document Frequency)
#vectorization because computer read words as number TF-IDF TF = how many times word appear, IDF = how many times word not appear
tfidf=TfidfVectorizer(max_features=2500)#2500 because computer does not slow down
x=tfidf.fit_transform(df["message"]).toarray()#convert message to matrix of numbers
y=df["target"].values
print(f"Rows in x: {len(x)}")
print(f"Rows in y: {len(y)}")

#detection engine
#train_test_split (80%training data, 20% new data)
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=42)
model=MultinomialNB()
model.fit(x_train, y_train)#learning of model will happer
y_pred=model.predict(x_test)#make prediction on test exam
# Displaying the results
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print(df.head())
