import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from python_crud import customer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
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
    logistic_model=LogisticRegression()
    knn_model=KNeighborsClassifier()
    decision_model=DecisionTreeClassifier()
    logistic_model.fit(x_train,y_train)
    knn_model.fit(x_train,y_train)
    decision_model.fit(x_train,y_train)
    print("""
    ==============================
    Training ML Models...
    ✔ Logistic Regression Trained
    ✔ KNN Trained
    ✔ Decision Tree Trained
    ==============================""")
    return logistic_model,knn_model,decision_model,scaler, x_test, y_test

def compareModels():
    logistic_model, knn_model, decision_model, scaler, x_test, y_test = trainModels()
    pred_logistic=logistic_model.predict(x_test)
    pred_knn=knn_model.predict(x_test)
    pred_decision=decision_model.predict(x_test)
    logistic_acc=accuracy_score(y_test,pred_logistic)
    knn_acc=accuracy_score(y_test,pred_knn)
    decision_acc=accuracy_score(y_test,pred_decision)
    print("============= Model Comparison =============")
    print("Logistic Regression :",logistic_acc)
    print("KNN                 :",knn_acc)
    print("Decision Tree       :",decision_acc)
    models={
        "Logistic Regression":logistic_acc,
        "KNN":knn_acc,
        "Decision Tree":decision_acc
    }
    if logistic_acc == knn_acc == decision_acc:
        print("🏆 All Models Perform Equally")
    else:
        best_models=max(models,key=models.get)
        print("Best Models          :",best_models)
        print("============================================")

compareModels()