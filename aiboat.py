import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from python_crud import customer
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

def Ailoans_Reports():
    df=pd.read_csv("Loan\customer.csv")
    print("AI LOAN ANALYSIS REPORT")
    print("================================================")
    print("Total Customers      :",len(df))
    safe = df[df["risk"] == "Safe"]
    risk = df[df["risk"] == "Risk"]
    print("Safe Customers       :",len(safe))
    print("Risk Customers       :",len(risk))
    avg_sal=df["salary"].mean()
    print("Average Salary       :",round(avg_sal,2))
    avg_loan=df["loan"].mean()
    print("Average Loan         :",round(avg_loan,2))
    avg_credit=df["credit"].mean()
    print("Average Credit Score :",round(avg_credit,2))
    h_salary=df["salary"].max()
    print("Highest Salary       :",h_salary)
    l_salary=df["salary"].min()
    print("Lowest Salary        :",l_salary)
    h_loan=df["loan"].max()
    print("Highest Loan         :",h_loan)
    l_loan=df["loan"].min()
    print("Lowest Loan          :",l_loan)
    per=df["risk"].value_counts(normalize=True)*100
    print("Safe Percentage      :",round(per["Safe"],2),"%")
    print("Risk Percentage      :",round(per["Risk"],2),"%")
    print("================================================")
    print("AI CONCLUSION")
    score=0
    if avg_credit>=700:
        print("✔ Customers have good credit history.")
        score+=1
    else:
        print("⚠ Some Customers Have Low Credit History")
    if round(per["Risk"],2)>40:
        print("⚠ High number of risky customers found.")
    else:
        print("✔ Majority of customers are Safe.")
        score+=1
    if avg_sal>50000:
        print("✔ Customers are financially stable.")
        score+=1
    else:
        print("⚠ Not All Customers are financially stable.")
    if avg_loan>500000:
        print("⚠ Average loan amount is high.")
    else:
        print("✔ Average loan amount is under control.")
        score+=1

    if score==4:
        print("✔ Dataset Status : Excellent")
    elif score==3:
        print("✔ Dataset Status : Good")
    elif score==2:
        print("✔ Dataset Status : Average")
    elif score<=1:
        print("⚠ Dataset Status : Poor")

    print("================================================")

def analyzCustomerByID():
    df=pd.read_csv("Loan\customer.csv")
    print("============= AI CUSTOMER REPORT =============")
    print("================================================")
    name=input("Enter Customer Name:")
    cust=df.loc[df["name"].str.lower()==name.lower()]
    if cust.empty:
        print("Customer Not Found")
    else:
        score=0
        customers=cust.iloc[0]
        if customers["salary"]>50000:
            print("Salary : High")
            score+=1
        else:
            print("Salary : Low")

        if customers["loan"]<customers["salary"]*2:
            print("Loan   : Low")
        elif customers["loan"]<customers["salary"]*5:
            score+=1
            print("Loan   : Moderate")
        elif customers["loan"]>=customers["salary"]*5:
            score+=1
            print("Loan   : Good")
    
        if customers["credit"]>=750:
            score+=1
            print("Credit : Excellent")
        elif customers["credit"]>=650 and customers["credit"]<750:
            score+=1
            print("Credit : Good")
        elif customers["credit"]>=550 and customers["credit"]<650:
            score+=1
            print("Credit : Average")
        else:
            print("Credit : Poor")
        
        if customers["exp"]<=1:
            print("Experience : Beginner")
        elif(customers["exp"]>=2 and customers["exp"]<5):
            score+=1
            print("Experience : Experienced")
        else:
            score+=1
            print("Experience : Highly Experienced")

        if customers["risk"]=="Safe":
            score+=1
            print("Risk : Safe")
        else:
            print("Risk : Risk")
        
        ratio=customers["loan"]/customers["salary"]
        if ratio>10:
            score+=1
            print("Status : High Risk")
        else:
            print("Status : Safe")
        print("================================================")
        print("Customer Details")
        print("Customer ID     :",customers["customer_id"])
        print("Customer Name   :",customers["name"])
        print("Customer Age    :",customers["age"])
        print("Customer Salary :",customers["salary"])
        print("Loan Amount     :",customers["loan"])
        print("Credit Score    :",customers["credit"])
        print("Risk            :",customers["risk"])
        print("================================================")
        print("AI DECISION")
        confidence=(score/6)*100
        if(confidence>=80):
            print("Confidence :",round(confidence,2),"%")
            print("Status     : Approved")
            print("✔ Strong Financial Profile")
            print("✔ Good Credit History")
            print("✔ Low Financial Risk")
        elif(confidence>=60 and confidence<=79):
            print("Confidence :",round(confidence,2),"%")
            print("Status     : REVIEW REQUIRED")
            print("✔ Customer is eligible.")
            print("⚠ Manual verification recommended.")
        else:
            print("Confidence :",round(confidence,2),"%")
            print("Status     : REJECTED")
            print("⚠ Poor Credit Score")
            print("⚠ High Loan Burden")
            print("⚠ Financial Risk is High")

def LoanApporvelSuggestion():
    print("============= AI LOAN APPORVEL SUGGESTIONS =============")
    print("================================================")
    name=input("Entet Name:")
    age=int(input("Enter Age:"))
    salary=int(input("Enter Salary:"))
    loan=int(input("Enter Loan Amount:"))
    credit=int(input("Enter Credit Score:"))
    experience=int(input("Enter How Many Year Of Exprience You Have:"))
    print("Reason")
    score=0
    if salary>=50000:
        score+=1
        print("✔ Salary above ₹50,000")
        print("✔ Good Salary")
    else:
        print("Low Salary")
    if credit>=700:
        score+=1
        print("✔ Credit Score above 700")
        print("✔ Excellent Credit")
    else:
        print("Poor Credit Score")
    if experience>=2:
        score+=1
        print("✔ Experience above 2 Years")
        print("✔ Good Experience")
    else: 
        print("⚠ Less Experience")
    if loan>salary*5:
        print("High Loan Amount")
        print("⚠ Loan is slightly high")
    else:
        score+=1
        print("✔ Loan Amount acceptable")
    if age >= 21:
        score += 1
        print("✔ Eligible Age")
    else:
        print("⚠ Age below loan eligibility")
    print("AI DECISION")
    print("================================================")
    confidence=(score/5)*100
    if(confidence>=95):
        print("Confidence     : Excellent Approval")
        print("Status         : Approved")
        print("Loan can be approved.")
        print("Customer has stable financial profile.")
    elif(confidence>=80 and confidence<95):
            print("Confidence : High")
            print("Status     : Approved")
            print("Loan can be approved.")
            print("Customer has stable financial profile.")
    elif(confidence>=60 and confidence<80):
            print("Confidence : Medium")
            print("Status     : Approved")
            print("Loan can be approved.")
            print("Customer has stable financial profile.")
    elif(confidence>=40 and confidence<60):
            print("Confidence : Very Low")
            print("Status     : Approved")
            print("Increase credit score.")
            print("Reduce loan amount.")
            print("Apply after 6 months.")
    else:
        print("Confidence : Low")
        print("Status     : Rejceted")
        print("Increase credit score.")
        print("Reduce loan amount.")
        print("Apply after 6 months.")

def highRiskReasonAnalysis():
    print("============= HIGH RISK REASON ANALYSIS =============")
    print("================================================")
    df=pd.read_csv("Loan\customer.csv")
    name=input("Enter Your Name:")
    customer_id=int(input("Enter Custmer ID:"))
    cust=df.loc[(df["name"].str.lower()==name.lower()) & (df["customer_id"]==customer_id)]
    if cust.empty:
        print("Custmer Not Found")
    else:
        user=cust.iloc[0]
        print("=-------------------------------- AI Riska Analysis --------------------------------------=")
        if user["credit"]<650:
            print("⚠ Credit Score is below the recommended limit (650).")
        else:
            print("Crdit Score Above 650")
        if user["loan"]>=user["salary"]*5:
            print("⚠ Loan amount is very high compared to salary.")
        else:
            print("Loan Amount is Okay")
        if user["salary"]<50000:
            print("⚠ Salary is below the preferred threshold.")
        else:
            print("Salary is Okay")
        raito=user["loan"]/user["salary"]
        if raito>10:
            print("Loan/Salary Ratio high")
        else:
            print("Loan/Salary Ratio Okay")
        if user["exp"]<2:
            print("Experience less than 2 Years")
        else:
            print("Experience is Okay")
        print("================================================")
        print("=-------------------- Recommendation: ---------------------------------=")
        if user["credit"]<650:
            print("Improve credit score")
        if user["loan"]>=user["salary"]*5:
                print("Reduce loan amount")
        if user["salary"]<50000:
            print("Increase income before applying again")
        if user["exp"]<2:
            print("Add More Experience")

def smartRecomandtion():
    print("============= SMART RECOMMENDDATIONS =============")
    print("================================================")
    df=pd.read_csv("Loan\customer.csv")
    avg_sal=df["salary"].mean()
    if avg_sal<50000:
        print("Increase salary requirement before approving loans")
    credit_h=df[df["credit"]>=650]
    credit_l=df[df["credit"]<650]
    if len(credit_l)>len(credit_h):
        print("Customers having Credit Score below 650 should be verified.")
    premium=df[(df["salary"]>=80000) & (df["risk"]=="Safe")]
    if len(premium)>0:
        print("Premium loan offers can be given to high salary customers")
    per=df["risk"].value_counts()
    safe=per["Safe"]
    risk=per["Risk"]
    if risk>=safe:
        print("Reduce loan approval for high-risk customers")
    ratio=df["loan"]/df["salary"]
    h_ratio=df[ratio>8]
    if len(h_ratio)>0:
        print("Review customers having high Loan/Salary Ratio")
    exp=df[df["exp"]<2]
    if len(exp)>0:
        print("Verify employment history before approving loans")
    print("============================ AI SUMMARY ==================================")
    if avg_sal>50000 and len(credit_l)<len(credit_h) and risk<safe and len(h_ratio)==0 and len(exp)==0:
        print("============= AI SUMMARY =============")
        print("No major issues found")
        print("Dataset looks healthy")
        print("======================================")
    else:
        print("============= AI SUMMARY =============")
        print("Dataset needs attention")
        print("Please follow the above recommendations")
        print("======================================")

def overAllDataHealth():
    print("============= SMART RECOMMENDDATIONS =============")
    print("================================================")
    df=pd.read_csv("Loan\customer.csv")
    miss_value=df.isnull().sum().sum()
    print("Missing Values    :",miss_value)
    duplicated=df.duplicated().sum()
    print("Duplicate Records :",duplicated)
    avg_credit=df["credit"].mean()
    if avg_credit >= 750:
        print("Average Credit : Excellent")
    elif avg_credit >= 700:
        print("Average Credit : Good")
    elif avg_credit >= 650:
        print("Average Credit : Average")
    else:
        print("Average Credit : Poor")
    per=df["risk"].value_counts(normalize=True)*100
    print("Risk Percentage    : ",round(per["Risk"],2),"%")
    print("Safe Percentage    : ",round(per["Safe"],2),"%")
    if miss_value==0 and duplicated==0 and avg_credit>=700 and round(per["Safe"],2)>round(per["Risk"],2):
        print("Dataset Status : HEALTHY")
        print("=========================== AI Opinion ============================")
        print("Dataset quality is excellent")
        print("Customer records are clean")
        print("Average credit score is good")
        print("Most customers are financially stable")
    elif miss_value==0 and duplicated==0 and avg_credit>=700 and round(per["Safe"],2)>round(per["Risk"],2):
        print("Dataset Status : HEALTHY")
        print("=========================== AI Opinion ============================")
        print("Dataset quality is excellent")
        print("Customer records are clean")
        print("Average credit score is good")
        print("Most customers are financially stable")
    elif miss_value==0 and duplicated==0 and avg_credit>=650 and avg_credit<=699 and round(per["Safe"],2)>round(per["Risk"],2):
        print("Dataset Status : AVERAGE")
        print("=========================== AI Opinion ============================")
        print("Dataset quality is excellent")
        print("Customer records are clean")
        print("Average credit score is good")
        print("Most customers are financially stable")
    else:
        print("Dataset Status : WEAK")
        print("=========================== AI Opinion ============================")
        print("Dataset requires attention")
        print("Credit score is below average")
        print("High risk customers should be reviewed")
        print("Data quality needs improvement")
def aiLoanAssistant():
    while True:
        print("""=============== AI LOAN ASSISTANT ===============
        1. Analyze Complete Dataset
        2. Analyze Customer by ID
        3. Loan Approval Suggestion
        4. High Risk Reason Analysis
        5. Smart Recommendations
        6. Overall Dataset Health
        7. Back
        =================================================""")
        choice=int(input("Choose a Option:"))
        if(choice==1):
            Ailoans_Reports()
        elif(choice==2):
            analyzCustomerByID()
        elif(choice==3):
            LoanApporvelSuggestion()
        elif(choice==4):
            highRiskReasonAnalysis()
        elif(choice==5):
            smartRecomandtion()
        elif(choice==6):
            overAllDataHealth()
        elif(choice==7):
            print("Back")
            break