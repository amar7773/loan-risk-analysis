import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from python_crud import customer
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics import accuracy_score,f1_score
import re
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
def preprocessText(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

def assistantData():
    data={"text": [
    "I want to check my loan risk",
    "Can you check my loan risk",
    "Check my risk",
    "Tell me my loan risk",
    "Am I eligible for a loan",
    "What is my loan eligibility",
    "Can I get a loan",
    "Can I apply for a loan",
    "Am I eligible",
    "What is credit score",
    "Tell me about credit score",
    "Why is credit score important",
    "How can I improve my credit score",
    "I want to improve my credit score",
    "How to increase credit score",
    "What is loan",
    "Tell me about loan",
    "Explain loan",
    "Hello",
    "Hi",
    "Hey",
    "Thank you",
    "Thanks"
],
"intent":[
    "risk_prediction",
    "risk_prediction",
    "risk_prediction",
    "risk_prediction",
    "eligibility",
    "eligibility",
    "eligibility",
    "eligibility",
    "eligibility",
    "credit_score",
    "credit_score",
    "credit_score",
    "improve_credit",
    "improve_credit",
    "improve_credit",
    "loan_info",
    "loan_info",
    "loan_info",
    "greeting",
    "greeting",
    "greeting",
    "thanks",
    "thanks"
]}
    df=pd.DataFrame(data)
    df["text"]=df["text"].apply(preprocessText)
    vectorizer=TfidfVectorizer()
    X=vectorizer.fit_transform(df["text"])
    y=df["intent"]
    model=LogisticRegression()
    model.fit(X,y)
    return model,vectorizer


def assistantResponse(intent):
    if intent == "greeting":
        return "Hello! 👋 I am your AI Loan Assistant. How can I help you?"
    elif intent == "thanks":
        return "You're welcome! 😊"
    elif intent == "risk_prediction":
        return "Sure! I can predict your loan risk. Please provide your age, salary, loan amount, credit score and experience."
    elif intent == "eligibility":
        return "I can help you check your loan eligibility. Please provide your salary, loan amount, credit score and experience."
    elif intent == "credit_score":
        return "Credit score helps determine your creditworthiness. A higher score generally indicates better credit health."
    elif intent == "improve_credit":
        return "You can improve your credit score by paying EMIs on time, keeping loan utilization under control and maintaining a good repayment history."
    elif intent == "loan_info":
        return "I can help you with loan risk, eligibility, credit score and loan-related information."
    else:   
        return "Sorry, I didn't understand your request."

    
def loadLoanModel():
    model = joblib.load("loan_risk_model.pkl")
    scaler = joblib.load("loan_scaler.pkl")
    encoder = joblib.load("risk_encoder.pkl")
    return model, scaler, encoder

def predictLoanRisk():
    model, scaler, encoder = loadLoanModel()
    age = int(input("Enter Age: "))
    salary = int(input("Enter Salary: "))
    loan = int(input("Enter Loan Amount: "))
    credit = int(input("Enter Credit Score: "))
    exp = int(input("Enter Experience: "))
    customer_data = pd.DataFrame(
        [[age, salary, loan, credit, exp]],
        columns=["age", "salary", "loan", "credit", "exp"]
    )
    customer_scaled = scaler.transform(customer_data)
    prediction = model.predict(customer_scaled)
    risk = encoder.inverse_transform(prediction)[0]
    probability = model.predict_proba(customer_scaled)
    prediction_index = list(model.classes_).index(prediction[0])
    risk_probability = probability[0][prediction_index]
    print("\n==============================================")
    print("          🤖 AI LOAN RISK PREDICTION")
    print("==============================================")
    print("Prediction  :", risk)
    print("Probability :", round(risk_probability * 100, 2), "%")
    if risk == "Safe":
        print("Status      : ✅ LOW RISK")
    else:
        print("Status      : ⚠️ HIGH RISK")
    print("==============================================")
    return risk, risk_probability

def predictIntent(text):
    text = preprocessText(text)
    model, vectorizer = assistantData()
    text_vect = vectorizer.transform([text])
    prediction = model.predict(text_vect)
    intent = prediction[0]
    print("Detected Intent:", intent)
    if intent == "risk_prediction":
        predictLoanRisk()
    else:
        response = assistantResponse(intent)
        print("AI Assistant:", response)

def compareTextModels():

    data = {
        "text": [
            "I want to check my loan risk",
            "Can you check my loan risk",
            "Check my risk",
            "Tell me my loan risk",

            "Am I eligible for a loan",
            "What is my loan eligibility",
            "Can I get a loan",
            "Can I apply for a loan",
            "Am I eligible",

            "What is credit score",
            "Tell me about credit score",
            "Why is credit score important",

            "How can I improve my credit score",
            "I want to improve my credit score",
            "How to increase credit score",

            "What is loan",
            "Tell me about loan",
            "Explain loan",

            "Hello",
            "Hi",
            "Hey",

            "Thank you",
            "Thanks"
        ],

        "intent": [
            "risk_prediction",
            "risk_prediction",
            "risk_prediction",
            "risk_prediction",

            "eligibility",
            "eligibility",
            "eligibility",
            "eligibility",
            "eligibility",

            "credit_score",
            "credit_score",
            "credit_score",

            "improve_credit",
            "improve_credit",
            "improve_credit",

            "loan_info",
            "loan_info",
            "loan_info",

            "greeting",
            "greeting",
            "greeting",

            "thanks",
            "thanks"
        ]
    }
    df = pd.DataFrame(data)
    df["text"] = df["text"].apply(preprocessText)
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["intent"],
        test_size=0.35,
        random_state=42,
        stratify=df["intent"]
    )
    # ==============================
    # BoW
    # ==============================
    bow = CountVectorizer()
    X_train_bow = bow.fit_transform(X_train)
    X_test_bow = bow.transform(X_test)
    bow_model = LogisticRegression(max_iter=1000)
    bow_model.fit(X_train_bow, y_train)
    bow_pred = bow_model.predict(X_test_bow)
    bow_accuracy = accuracy_score(y_test, bow_pred)
    bow_f1 = f1_score(y_test, bow_pred, average="weighted")
    # ==============================
    # TF-IDF
    # ==============================
    tfidf = TfidfVectorizer()
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    tfidf_model = LogisticRegression(max_iter=1000)
    tfidf_model.fit(X_train_tfidf, y_train)
    tfidf_pred = tfidf_model.predict(X_test_tfidf)
    tfidf_accuracy = accuracy_score(y_test, tfidf_pred)
    tfidf_f1 = f1_score(y_test, tfidf_pred, average="weighted")
    result = pd.DataFrame({
        "Method": ["BoW", "TF-IDF"],
        "Accuracy": [
            round(bow_accuracy * 100, 2),
            round(tfidf_accuracy * 100, 2)
        ],
        "F1 Score": [
            round(bow_f1 * 100, 2),
            round(tfidf_f1 * 100, 2)
        ]
    })
    print("\n==============================================")
    print("           BoW vs TF-IDF")
    print("==============================================")
    print(result.to_string(index=False))
    return result

def saveAssistantModel():
    model, vectorizer = assistantData()
    joblib.dump(model, "loan_assistant_model.pkl")
    joblib.dump(vectorizer, "loan_assistant_vectorizer.pkl")
    print("NLP Model Saved Successfully")

saveAssistantModel()