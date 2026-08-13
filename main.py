from fastapi import FastAPI
from pydantic import BaseModel,Field
import pandas as pd
import joblib

app=FastAPI(    
    title="AI Loan Risk Assistant",
    description="Loan Risk Prediction API",
    version="1.0")
model = joblib.load("loan_risk_model.pkl")
scaler = joblib.load("loan_scaler.pkl")
encoder = joblib.load("risk_encoder.pkl")
assistant_model = joblib.load("loan_assistant_model.pkl")
assistant_vectorizer = joblib.load("loan_assistant_vectorizer.pkl")

class CustomerData(BaseModel):
    age: int
    salary: int
    loan: int
    credit: int
    exp: int

class AssistantRequest(BaseModel):
    text: str
    age: int | None = None
    salary: int | None = None
    loan: int | None = None
    credit: int | None = None
    exp: int | None = None

@app.get("/")
def home():
    return{
        "message":"AI Loan Risk Assistant API is running"
    }

@app.post("/predict")
def predict(customer:CustomerData):
    data=pd.DataFrame([[
        customer.age,
        customer.salary,
        customer.loan,
        customer.credit,
        customer.exp
    ]],
    columns=[  "age",
            "salary",
            "loan",
            "credit",
            "exp"
        ]
    )
    data_scaled=scaler.transform(data)
    prediction=model.predict(data_scaled)
    risk=encoder.inverse_transform(prediction)[0]
    probability=model.predict_proba(data_scaled)
    prediction_index = list(model.classes_).index(prediction[0])
    probability_value = probability[0][prediction_index]
    return{
        "prediction": risk,
        "probability": round(float(probability_value) * 100, 2),
        "status": "LOW RISK" if risk == "Safe" else "HIGH RISK"
    }
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

@app.post("/assitant")
def assitant(request:AssistantRequest):
    text_vector=assistant_vectorizer.transform([request.text])
    prediction=assistant_model.predict(text_vector)
    intent=prediction[0]
    if intent == "risk_prediction":
        if None in [
            request.age,
            request.salary,
            request.loan,
            request.credit,
            request.exp
        ]:
            return {
                "question": request.text,
                "intent": intent,
                "response": "Please provide age, salary, loan amount, credit score and experience."
            }
        data = pd.DataFrame([[
            request.age,
            request.salary,
            request.loan,
            request.credit,
            request.exp
        ]],
        columns=[
            "age",
            "salary",
            "loan",
            "credit",
            "exp"
        ])
        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)
        risk = encoder.inverse_transform(prediction)[0]
        probability = model.predict_proba(data_scaled)
        prediction_index = list(model.classes_).index(prediction[0])
        probability_value = probability[0][prediction_index]
        return {
            "question": request.text,
            "intent": intent,
            "prediction": risk,
            "probability": round(float(probability_value) * 100, 2),
            "status": "LOW RISK" if risk == "Safe" else "HIGH RISK"
        }
    response = assistantResponse(intent)
    return {
        "question": request.text,
        "intent": intent,
        "response": response
    }