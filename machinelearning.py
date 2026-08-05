import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from python_crud import customer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score
def trainModels():
    df=pd.read_csv("Loan\customer.csv")
    copy_df=df.copy()
    le=LabelEncoder()
    copy_df["risk"]=le.fit_transform(copy_df["risk"])
    X=copy_df[["age","salary","loan","credit","exp"]]
    y=copy_df["risk"]
    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    scaler=StandardScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)
    models={
        "Logistic Regression":LogisticRegression(),
        "KNN":KNeighborsClassifier(n_neighbors=3),
        "Decision Tree":DecisionTreeClassifier(),
        "Naive Bayes":GaussianNB(),
        "SVM":SVC(kernel="rbf")
    }
    print("\n========== Training ML Models ==========\n")
    for name,model in models.items():
        model.fit(x_train,y_train)
        print(f"✔ {name} Trained")
    print("\n========================================\n")
    return models,scaler, x_test, y_test

def compareModels():
    models,scaler, x_test, y_test = trainModels()
    accuracies={}
    print("\n========== Model Comparison ==========\n")
    for name,model in models.items():
        prediction=model.predict(x_test)
        acc=accuracy_score(y_test,prediction)
        accuracies[name]=acc
        print(f"{name:22} : {round(acc*100,2)}")
    print()
    if(len(set(accuracies.values()))==1):
        print("🏆 All Models Perform Equally")
        print("Using Decision Tree for Prediction")
        best_name="Decision Tree"
    else:
        best_name=max(accuracies,key=accuracies.get)
        print(f"Best Model :{best_name}")
    best_model=models[best_name]
    print("\n======================================\n")
    return best_name, best_model, scaler

compareModels()