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
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score
def trainModels():
    df=pd.read_csv("Loan\customer.csv")
    copy_df=df.copy()
    le=LabelEncoder()
    copy_df["risk"]=le.fit_transform(copy_df["risk"])
    X=copy_df[["age","salary","loan","credit","exp"]]
    y=copy_df["risk"]
    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
    scaler=StandardScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)
    models={
        "Logistic Regression":LogisticRegression(),
        "KNN":KNeighborsClassifier(n_neighbors=3),
        "Decision Tree":DecisionTreeClassifier(random_state=42),
        "Naive Bayes":GaussianNB(),
        "SVM":SVC(kernel="rbf",random_state=42)
    }
    print("\n========== Training ML Models ==========\n")
    for name,model in models.items():
        model.fit(x_train,y_train)
        print(f"✔ {name} Trained")
    print("\n========================================\n")
    return models,scaler, x_test, y_test,x_train,y_train

def compareModels():
    models, scaler, x_test, y_test, x_train, y_train = trainModels()
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
        print(f"Best Model   :{best_name}")
    print("\n======================================\n")
    print(f"Best Accuracy :{round(accuracies[best_name]*100,2)}%")
    print(f"Total Models  :{len(models)}")
    best_model=models[best_name]
    print("\n======================================\n")
    return best_name, best_model, scaler

def tuneBestModel():
    models, scaler, x_test, y_test, x_train, y_train = trainModels()
    best_name, best_model, scaler = compareModels()
    if best_name=="Decision Tree":
        grid=GridSearchCV(DecisionTreeClassifier(random_state=42),
            param_grid={
                "criterion": ["gini", "entropy"],
                "max_depth": [3, 5, 10, 15, None],
                "min_samples_split": [2, 5, 10],
                 "min_samples_leaf": [1, 2, 4]},cv=3,return_train_score=False,n_jobs=-1)
    elif best_name=="SVM":
        grid=GridSearchCV(SVC(random_state=42),
            param_grid={
           "C": [0.1, 1, 10, 100],
           "kernel": ["linear", "rbf"],
            "gamma": ["scale", "auto"]},cv=3,return_train_score=False,n_jobs=-1)
    elif best_name=="Logistic Regression":
        grid=GridSearchCV(LogisticRegression(max_iter=1000),
            param_grid = {
            "C": [0.01, 0.1, 1, 10, 100],
            "penalty": ["l2"],
            "solver": ["lbfgs", "liblinear"]},cv=3,return_train_score=False,n_jobs=-1)
    else:
        print("No Hyperparameter Tuning Required")
        return best_name, best_model, scaler
    
    grid.fit(x_train,y_train)
    print("Best Model           :",best_name)
    print("Best Params          :",grid.best_params_)
    print(f"Best Score          :{round(grid.best_score_*100,2)}%")
    tuned_model=grid.best_estimator_
    test_prediction=tuned_model.predict(x_test)
    test_acc=accuracy_score(y_test,test_prediction)
    print(f"Test Accuracy Score :{round(test_acc*100,2)}%")
    print("\n==========================================\n")
    return best_name,tuned_model,scaler

def predictCustomerRisk():
    best_name, best_model, scaler=compareModels()
    print("============= AI LOAN ASSISTANT =============")
    age=float(input("Enter Age :"))
    salary=float(input("Enter Salary :"))
    loan=float(input("Enter Loan Amount :"))
    credit=float(input("Enter Credit Score :"))
    exp=float(input("Enter Experience :"))
    new_data=[[age,salary,loan,credit,exp]]
    new_data=scaler.transform(new_data)
    predicton=best_model.predict(new_data)[0]
    print("Selected Model Name :", best_name)
    if predicton==0:
        print("Prediction          : RISK")
    else:
        print("Prediction          : SAFE")
    print("============= AI ANALYSIS =============")
    if salary>50000:
        print("✔ High Salary")
    else:
        print("Low Salary")
    if credit>=750:
        print("✔ Excellent Credit Score")
    elif credit>=600 and credit<750:
        print("✔ Good Credit Score")
    elif credit>500 and credit<600:
        print("✔ Average Credit Score")
    else:
        print("Poor Credit Score")
    if exp>=2:
        print("✔ Sufficient Experience")
    else:
        print("Less Experience")
    if loan<=salary*5:
        print("✔ Loan Amount Acceptable")
    else:
        print("Loan Amount not Acceptable")
    if predicton==1:
        print("🤖 Recommendation : Loan Approved")
    else:
        print("🤖 Recommendation : Loan Rejected")
    print("=======================================")
def malModels():
    while True:
        print("""=============== Machine Learning ===============
        1. Train Models
        2. Compare Models
        3. Hyperparameter Tuning
        4. Ensemble Learning
        5. Predict Customer Risk
        6. Model Performance
        7. Back
        ===============================================""")
        choice=int(input("Choose a Option :"))
        if(choice==1):
            trainModels()
        elif(choice==2):
            compareModels()
        elif(choice==3):
            tuneBestModel()
        elif(choice==5):
            predictCustomerRisk()
        elif(choice==7):
            print("Back to Main Menu")
            break

malModels()