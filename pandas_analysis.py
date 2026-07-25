import json
import numpy as np
import pandas as pd
from python_crud import customer

def generateCustomerReport():
    df=pd.read_csv("Loan\customer.csv")
    print("============= CUSTOMER REPORT =============")
    print("Total Customer's:",len(df))
    print("Average Salary:",df["salary"].mean())
    print("Average Loan:",df["loan"].mean())
    h_salary=df["salary"].sort_values(axis=0,ascending=False)
    print("Highest Salary:",h_salary.iloc[0])
    l_salary=df["salary"].sort_values(axis=0,ascending=True)
    print("Lowest Salary:",l_salary.iloc[0])
    h_loan=df["loan"].sort_values(axis=0,ascending=False)
    print("Highest Loan:",h_loan.iloc[0])
    l_loan=df["loan"].sort_values(axis=0,ascending=True)
    print("Lowest Loan:",l_loan.iloc[0])
    total_missing=df.isnull().sum().sum()
    print("Total Missing Values:",total_missing)
    print("Total Columns:",len(df.columns))
    print("===========================================")

def analyzeSalary():
    df=pd.read_csv("Loan\customer.csv")
    print("=============== Salary Analysis ===============")
    print("Average Salary:",df["salary"].mean())
    print("Median Salary:",df["salary"].median())
    print("Standard Deviation:",df["salary"].std())
    print("")
    print("Highest Salary:",df["salary"].max())
    print("Lowest Salary:",df["salary"].min())
    print("Top 5 Highest Salary Customer's:")
    print("--------------------------------")
    h_salary=df.sort_values(by=["salary"],axis=0,ascending=False)
    print(h_salary.head(5))
    print("Top 5 Lowest Salary Customer's:")
    print("--------------------------------")
    l_salary=df.sort_values(by=["salary"],axis=0,ascending=True)
    print(l_salary.head(5))
    print("=========================================")

def analyzeLoan():
    df=pd.read_csv("Loan\customer.csv")
    print("=============== Loan Analysis ===============")
    print("Average Loan:",df["loan"].mean())
    print("Median Loan:",df["loan"].median())
    print("Standard Deviation:",df["loan"].std())
    print("Highest Loan:",df["loan"].max())
    print("Lowest Loan:",df["loan"].min())
    print("Top 5 Highest Loan Customer's:")
    print("--------------------------------")
    print(df.nlargest(5,"loan"))
    print("Top 5 Lowest Loan Customer's:")
    print("--------------------------------")
    print(df.nsmallest(5,"loan"))
    print("=========================================")

def analyzeRisk():
    df=pd.read_csv("Loan\customer.csv")
    print("=============== Risk Analysis ===============")
    var_count=df.groupby("risk")
    safe_cust=var_count.get_group("Safe")
    safe=len(safe_cust)
    print("Safe Customer's:",safe)
    risk_cust=var_count.get_group("Risk")
    risk=len(risk_cust)
    print("Risk Customer's:",risk)
    total=safe+risk
    print("Safe Customer's Percentage :",safe/total*100)
    print("Risk Customer's Percentage :",risk/total*100)
    print("Highest Risk Customer Loan :",risk_cust["loan"].max())
    print("Highest Risk Customer Salary :",risk_cust["salary"].max())
    print("=========================================")

def searchCustomer():
    while True:
        print("========== Search Customer ==========")
        print("1. Search By Name")
        print("2. Search By Salary")
        print("3. Search By Loan")
        print("4. Search By Credit Score")
        print("5. Search By Risk")
        print("6. Search By Experience")
        print("7. Back")
        df=pd.read_csv("Loan\customer.csv")
        choice=int(input("Enter Choice for Search Customer:"))
        if(choice==1):
            name=input("Enter Your Name:")
            s_name=df.loc[df["name"].str.lower()==name.lower()]
            if s_name.empty:
                print("Customer Not Found")
            else:
                print(s_name)
        elif(choice==2):
            salary=int(input("Enter Your Minimum Salary:"))
            result_s=df.loc[df["salary"]==salary]
            if result_s.empty:
                print("Customer Not Found")
            else:
                print(result_s)
        elif(choice==3):
            loan=int(input("Enter Your Minimum Loan:"))
            result_l=df.loc[df["loan"]==loan]
            if result_l.empty:
                print("Customer Not Found")
            else:
                print(result_l)
        elif(choice==4):
            credit=int(input("Enter Credit Score:"))
            result_c=df.loc[df["credit"]==credit]
            if result_c.empty:
                print("Customer Not Found")
            else:
                print(result_c)
        elif(choice==5):
            risk=input("Enter Risk/Safe:")
            result_r=df.loc[df["risk"].str.lower()==risk.lower()]
            if result_r.empty:
                print("Customer Not Found")
            else:
                print(result_r)
        elif(choice==6):
            exp=int(input("Enter Your Minimum Exprience:"))
            result_exp=df.loc[df["salary"]==exp]
            if result_exp.empty:
                print("Customer Not Found")
            else:
                print(result_exp)
        elif(choice==7):
            print("Exit")
            break
        else:
            print("You Enter Wrong Choice")

def manageDataCleaning():
    while True:
        print("""========== Data Cleaning ==========
        =================================================
        1. Show Missing Values
        2. Fill Missing Salary
        3. Fill Missing Loan
        4. Replace Risk Values
        5. Remove Duplicate Customers
        6. Remove Missing Rows
        7. Back 
        =================================================""")
        df=pd.read_csv("Loan\customer.csv")
        choice=int(input("Enter Your Choice:"))
        if(choice==1):
             print("Total Missing Values:",df.isnull().sum(True).sum())
        elif(choice==2):
            salary=int(input("Enter To fill The Missing Salary:"))
            df["salary"]=df["salary"].fillna(salary)
            df.to_csv("Loan\customer.csv",index=False)
            print(df)
        elif(choice==3):
            loan=int(input("Enter To fill The Missing Loan:"))
            df.to_csv("Loan\customer.csv",index=False)
            df["loan"]=df["loan"].fillna(loan)
            df.to_csv("Loan\customer.csv",index=False)
            print(df)
        elif(choice==4):
            df["risk"]=df["risk"].replace({
            "Risk":"High Risk",
            "Safe":"Low Risk"
        })
            df.to_csv("Loan\customer.csv",index=False)
            print("Risk values replaced successfully!")
            print(df)
        elif(choice==5):
            df=df.drop_duplicates()
            df.to_csv("Loan\customer.csv",index=False)
            print("Remove Duplicate's Customer's Successfuly")
            print(df)
        elif (choice==6):
            df=df.dropna()
            df.to_csv("Loan\customer.csv",index=False)
            print("Remove Missing Row's Successfuly")
            print(df)
        elif(choice==7):
            print("Exit")
        else:
            print("You Entered Wrong Choice")


def pandaAnalyz():
     while True:
            print("\n---------------- Pandas Analytics -------------------")
            print("1. Customer Report")
            print("2. Salary Analysis")
            print("3. Loan Analysis")
            print("4. Risk Analysis")
            print("5. Customer Search")
            print("6. Data Cleaning")
            print("7. Back")
            choice = int(input("Choose Your Option : "))
            if (choice==1):
                generateCustomerReport()
            elif(choice==2):
                analyzeSalary()
            elif(choice==3):
                analyzeLoan()
            elif(choice==4):
                analyzeRisk()
            elif(choice==5):
                searchCustomer()
            elif(choice==6):
                manageDataCleaning()
            elif(choice==7):
                print("Returning to Main Menu...")
                break
            else:
                print("You Enterd Wrong Choice")