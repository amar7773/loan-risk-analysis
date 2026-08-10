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
from sklearn.model_selection import train_test_split,GridSearchCV,RandomizedSearchCV
from sklearn.ensemble import StackingClassifier,RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

def trainModel():
    df=pd.read_csv("customer.csv")
    print("Dataset Loaded Successfully")
    print("Rows          :",len(df))
    print("Coulmns       :",len(df.columns))
    print("Missing Values:",df.isnull().sum().sum())
    print("Dataset Ready")
    X=df[['age', 'salary', 'loan', 'credit', 'exp']]
    le=LabelEncoder()
    df["risk"]=le.fit_transform(df["risk"])
    y=df["risk"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    models=RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    models.fit(X_train,y_train)
    print("✔ Random Forest Model Trained Successfully")
    print("\n==============================================")
    return models,le,X_test,y_test

def evaluateModel():
    models,le,X_test,y_test=trainModel()
    y_pred=models.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    precision=precision_score(y_test,y_pred)
    recall=recall_score(y_test,y_pred)
    f1=f1_score(y_test,y_pred)
    cm=confusion_matrix(y_test,y_pred)
    print(f"Accuracy Score  :{round(accuracy*100,2)}%")
    print(f"Preicsion Score :{round(precision*100,2)}%")
    print(f"Recall Score    :{round(recall*100,2)}%")
    print(f"F1 Score        :{round(f1*100,2)}%")
    print("Confusion Matrix :")
    print(cm)
    return accuracy, precision, recall, f1, cm

def predictNewCustomer():
    models,le,X_test,y_test=trainModel()
    age=int(input("Enter Age :"))
    salary=int(input("Enter Salary :"))
    loan=int(input("Enter Loan :"))
    credit=int(input("Enter Credit Score :"))
    experience=int(input("Enter Experience :"))
    new_customer=pd.DataFrame([[age,salary,loan,credit,experience]],columns=["age", "salary", "loan", "credit", "exp"])
    new_pred=models.predict(new_customer)
    result = le.inverse_transform(new_pred)[0]
    probability=models.predict_proba(new_customer)
    predict_index=list(models.classes_).index(new_pred)
    prediction_prob=probability[0][predict_index]   
    print("\n==============================================")
    print("          🤖 AI LOAN RISK PREDICTION")
    print("==============================================")
    print("Age          :",age)
    print("Salary       :",salary)
    print("Loan         :",loan)
    print("Credit Score :",credit)
    print("Experience   :",experience)
    print("----------------------------------------------")
    print("Prediction   :",result)
    print("Probability  :",round(prediction_prob*100,2),"%")
    print("==============================================")
    if result=="Safe":
        print("Status          : ✅ LOW RISK")
    else:
        print("Status          : ⚠️ HIGH RISK")
    print("==============================================")

def compareModels():
    df=pd.read_csv("customer.csv")
    X=df[['age', 'salary', 'loan', 'credit', 'exp']]
    le=LabelEncoder()
    df["risk"]=le.fit_transform(df["risk"])
    y=df["risk"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    result=[]
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    trained_models = {}
    models={
        "Logistic Regression":(LogisticRegression(max_iter=1000),True),
        "KNN":(KNeighborsClassifier(n_neighbors=5),True),
        "Decision Tree":(DecisionTreeClassifier(random_state=42),False),
        "Random Forest":(RandomForestClassifier(n_estimators=100,random_state=42),False),
        "Naive Bayes":(GaussianNB(),False),
        "SVM":(SVC(),True),
        "Gradient Boosting":(GradientBoostingClassifier(random_state=42),False)
    }
    for name,(model,use_scaling) in models.items():
        if use_scaling:
            model.fit(X_train_scaled,y_train)
            y_pred=model.predict(X_test_scaled)
        else:
            model.fit(X_train,y_train)
            y_pred=model.predict(X_test)
        accuracy=accuracy_score(y_test,y_pred)
        precision=precision_score(y_test,y_pred)
        recall=recall_score(y_test,y_pred)
        f1=f1_score(y_test,y_pred)
        result.append({
        "Model":name,
        "Accuracy":f"{round(accuracy*100,2)}%",
        "Precision":f"{round(precision*100,2)}%",
        "Recall":f"{round(recall*100,2)}%",
        "F1_Score":f"{round(accuracy*100,2)}%"
    })
        trained_models[name]=model
    print("\n==============================================")
    print("             MODEL COMPARISON")
    print("==============================================")
    result_df=pd.DataFrame(result)
    print(result_df.to_string(index=False))
    best_row=result_df.loc[result_df["F1_Score"].idxmax()]
    best_model_name=best_row["Model"]
    best_model=trained_models[best_model_name]
    best_score=best_row["F1_Score"]
    print("Best Model Name :",best_model_name)
    print("Best Model      :",best_model)
    print("Best Score      :",best_score)
    return(best_model_name,best_model,scaler,le,result_df)
compareModels()