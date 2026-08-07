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
from sklearn.metrics import accuracy_score

def trainModels():
    df = pd.read_csv("Loan/customer.csv")
    copy_df = df.copy()
    le = LabelEncoder()
    copy_df["risk"] = le.fit_transform(copy_df["risk"])
    X = copy_df[["age", "salary", "loan", "credit", "exp"]]
    y = copy_df["risk"]
    x_train, x_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "KNN": KNeighborsClassifier(n_neighbors=3),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Naive Bayes": GaussianNB(),
        "SVM": SVC(kernel="rbf", random_state=42)
    }
    print("\n========== Training ML Models ==========\n")
    for name, model in models.items():
        model.fit(x_train, y_train)
        print(f"✔ {name} Trained Successfully")
    print("\n========================================\n")
    return models, scaler, x_train, x_test, y_train, y_test

def compareModels(models, x_test, y_test):
    models, scaler, x_train, x_test, y_train, y_test = trainModels()
    accuracies = {}
    print("\n========== Model Comparison ==========\n")
    for name, model in models.items():
        prediction = model.predict(x_test)
        acc = accuracy_score(y_test, prediction)
        accuracies[name] = acc
        print(f"{name:22} : {acc*100:.2f}%")
    print()
    if len(set(accuracies.values())) == 1:
        print("🏆 All Models Perform Equally")
        print("Using Decision Tree for Prediction")
        best_name = "Decision Tree"
    else:
        best_name = max(accuracies, key=accuracies.get)
    best_model = models[best_name]
    print(f"Best Model     : {best_name}")
    print(f"Best Accuracy  : {accuracies[best_name]*100:.2f}%")
    print(f"Total Models   : {len(models)}")
    print("\n======================================\n")
    return (
        best_name,
        best_model,
        scaler,
        x_train,
        x_test,
        y_train,
        y_test
    )
def tuneBestModel():
    models, scaler, x_train, x_test, y_train, y_test = trainModels()
    best_name, best_model = compareModels(models,x_test,y_test)
    if best_name == "Decision Tree":
        grid = GridSearchCV(
            DecisionTreeClassifier(random_state=42),
            param_grid={
                "criterion": ["gini", "entropy"],
                "max_depth": [3, 5, 10, 15, None],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4]
            },
            cv=3,
            n_jobs=-1
        )
    elif best_name == "SVM":
        grid = GridSearchCV(
            SVC(random_state=42),
            param_grid={
                "C": [0.1,1,10,100],
                "kernel":["linear","rbf"],
                "gamma":["scale","auto"]
            },
            cv=3,
            n_jobs=-1
        )
    elif best_name == "Logistic Regression":
        grid = GridSearchCV(
            LogisticRegression(max_iter=1000),
            param_grid={
                "C":[0.01,0.1,1,10,100],
                "penalty":["l2"],
                "solver":["lbfgs","liblinear"]
            },
            cv=3,
            n_jobs=-1
        )
    else:
        print("No Hyperparameter Tuning Required")
        return best_name, best_model, scaler
    print("\n========== Hyperparameter Tuning ==========\n")
    grid.fit(x_train,y_train)
    tuned_model = grid.best_estimator_
    prediction = tuned_model.predict(x_test)
    accuracy = accuracy_score(y_test,prediction)
    print("Best Model  :",best_name)
    print("Best Params :",grid.best_params_)
    print(f"CV Score    : {grid.best_score_*100:.2f}%")
    print(f"Test Score  : {accuracy*100:.2f}%")
    print("\n===========================================\n")
    return best_name,tuned_model,scaler

def ensembleLearning():
    models, scaler, x_train, x_test, y_train, y_test = trainModels()
    print("\n========== Ensemble Learning ==========\n")
    # Bagging
    bag_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    bag_model.fit(x_train,y_train)
    bag_acc = accuracy_score(
        y_test,
        bag_model.predict(x_test)
    )
    # Boosting
    boost_model = AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=1),
        n_estimators=100,
        random_state=42
    )
    boost_model.fit(x_train,y_train)
    boost_acc = accuracy_score(
        y_test,
        boost_model.predict(x_test)
    )
    # Stacking
    base_models = [
        ("lr",LogisticRegression(max_iter=1000)),
        ("svm",SVC()),
        ("dt",DecisionTreeClassifier())
    ]
    stack_model = StackingClassifier(
        estimators=base_models,
        final_estimator=LogisticRegression(max_iter=1000)
    )
    stack_model.fit(x_train,y_train)
    stack_acc = accuracy_score(
        y_test,
        stack_model.predict(x_test)
    )
    accuracies={
        "Bagging":bag_acc,
        "Boosting":boost_acc,
        "Stacking":stack_acc
    }
    print(f"Bagging   : {bag_acc*100:.2f}%")
    print(f"Boosting  : {boost_acc*100:.2f}%")
    print(f"Stacking  : {stack_acc*100:.2f}%")
    best=max(accuracies,key=accuracies.get)
    print("-------------------------------------")
    print("Best Ensemble :",best)
    print(f"Accuracy      : {accuracies[best]*100:.2f}%")
    print("=====================================\n")
    return best

def predictCustomerRisk():
    best_name, tuned_model, scaler = tuneBestModel()
    print("\n========== AI LOAN ASSISTANT ==========\n")
    age = int(input("Enter Age : "))
    salary = float(input("Enter Salary : "))
    loan = float(input("Enter Loan Amount : "))
    credit = int(input("Enter Credit Score : "))
    exp = float(input("Enter Experience : "))
    new_data = [[age, salary, loan, credit, exp]]
    new_data = scaler.transform(new_data)
    prediction = tuned_model.predict(new_data)[0]
    print("\n========== Prediction ==========\n")
    print("Selected Model :", best_name)
    if prediction == 1:
        print("Prediction     : SAFE")
    else:
        print("Prediction     : RISK")
    # Confidence Score
    if hasattr(tuned_model, "predict_proba"):
        confidence = max(tuned_model.predict_proba(new_data)[0]) * 100
        print(f"Confidence     : {confidence:.2f}%")
    print("\n========== AI Analysis ==========\n")
    # Salary
    if salary >= 70000:
        print("✔ Excellent Salary")
    elif salary >= 50000:
        print("✔ Good Salary")
    else:
        print("✘ Low Salary")
    # Credit Score
    if credit >= 750:
        print("✔ Excellent Credit Score")
    elif credit >= 650:
        print("✔ Good Credit Score")
    elif credit >= 550:
        print("⚠ Average Credit Score")
    else:
        print("✘ Poor Credit Score")
    # Experience
    if exp >= 5:
        print("✔ Experienced Customer")
    elif exp >= 2:
        print("✔ Sufficient Experience")
    else:
        print("✘ Less Experience")
    # Loan Analysis
    loan_ratio = loan / salary
    if loan_ratio <= 5:
        print("✔ Loan Amount Acceptable")
    elif loan_ratio <= 8:
        print("⚠ Loan Amount is High")
    else:
        print("✘ Loan Amount is Very High")
    print("\n========== Final Recommendation ==========\n")
    if prediction == 1:
        print("🤖 Recommendation : LOAN APPROVED")
    else:
        print("🤖 Recommendation : LOAN REJECTED")
    print("\n==========================================\n")

def malModels():
    while True:
        print("""
        ================ Machine Learning ================
        1. Train Models
        2. Compare Models
        3. Hyperparameter Tuning
        4. Ensemble Learning
        5. Predict Customer Risk
        6. Model Performance
        7. Back==================================================""")
        try:
            choice = int(input("Choose an Option : "))
            if choice == 1:
                trainModels()
            elif choice == 2:
                compareModels()
            elif choice == 3:
                tuneBestModel()
            elif choice == 4:
                ensembleLearning()
            elif choice == 5:
                predictCustomerRisk()
            elif choice == 7:
                print("Back to Main Menu...")
                break
            else:
                print("❌ Invalid Choice")
        except ValueError:
            print("❌ Please Enter Numbers Only.")

malModels()