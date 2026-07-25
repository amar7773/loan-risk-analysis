import json
import numpy as np
from python_crud import customer

def salaryStatistics():
    print("================ Salary Statistics ================")
    salary = []
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    salaries = np.array(salary)
    print("Average Salary :", np.mean(salaries))
    print("Median Salary :", np.median(salaries))
    print("Standard Deviation :", np.std(salaries))
    per = int(input("Enter Percentile : "))
    print(f"{per} Percentile Salary :", np.percentile(salaries, per))

def creditStatistics():
    print("\n========== Credit Statistics ==========")
    credits = []
    for customer_id in customer:
        credits.append(customer[customer_id]["credit"])
    credits = np.array(credits)
    print("Average Credit :", np.mean(credits))
    print("Highest Credit :", np.max(credits))
    print("Lowest Credit :", np.min(credits))

def countTotalCustomers():
    print("=================Total Customer's=======================")
    total=[]
    for customer_id in customer:
        total.append( customer.keys())
    total_customer=np.array(total)
    print("Total Customer's:",total_customer.size)

def displayHighRiskCustomers():
    print("===============High Risk Customers=======================")
    risk=[]
    for customer_id in customer:
        risk.append(customer[customer_id]["risk"])
    risks=np.array(risk)
    total_risk=np.sum(risk=="Risk")
    print("Total High Risk Customer's:",total_risk)
    for customer_id in customer:
        if customer[customer_id]["risk"]=="Risk":
            print("Customer ID:",customer_id)
            print("Customer Name:",customer[customer_id]["name"])
            print("Customer Age:",customer[customer_id]["age"])
            print("Customer Salary:",customer[customer_id]["salary"])
            print("Loan Amount:",customer[customer_id]["loan"])
            print("Credit Score:",customer[customer_id]["credit"])
            print("Experience:",customer[customer_id]["exp"])
            print("==================================")
            break
        else:
            print("No Risk Customer's!")

def displayHighSalaryCustomers():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    salaries=np.array(salary)
    high_salary=salaries[salaries>50000]
    if len(high_salary)==0:
        print("No High Lvel Customer!")
    else:
        print("Total High Level Salary Customer's:",len(high_salary))
    print("==================================")
    for customer_id in customer:
        if customer[customer_id]["salary"]>50000:
            print("Customer ID:",customer_id)
            print("Customer Name:",customer[customer_id]["name"])
            print("Customer Age:",customer[customer_id]["age"])
            print("Customer Salary:",customer[customer_id]["salary"])
            print("Loan Amount:",customer[customer_id]["loan"])
            print("Credit Score:",customer[customer_id]["credit"])
            print("Experience:",customer[customer_id]["exp"])
            print("==================================")

def calculateLoanToSalaryRatio():
    print("==================================")
    salary=[]
    loan=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
        loan.append(customer[customer_id]["loan"])
    salaries=np.array(salary)
    loans=np.array(loan)
    ratio=loans/salaries
    print("Ratio:",ratio)
    print("==================================")
    for i,customer_id in enumerate(customer):
        print("Customer ID:",customer_id)
        print("Customer Name:",customer[customer_id]["name"])
        print("Customer Age:",customer[customer_id]["age"])
        print("Customer Salary:",customer[customer_id]["salary"])
        print("Loan Amount:",customer[customer_id]["loan"])
        print("Credit Score:",customer[customer_id]["credit"])
        print("Ratio:",round(ratio[i],2))
        if ratio[i] > 10:
            print("Status : High Risk")
        else:
            print("Status : Safe")
        print("==================================")

def analyzeLoanDistribution():
    loan=[]
    for customer_id in customer:
        loan.append(customer[customer_id]["loan"])
    loans=np.array(loan)
    count1=0
    count2=0
    count3=0
    count4=0
    for l in loans:
        if l>0 and l<100000:
            count1+=1
        elif l>=100000 and l<500000:
            count2+=1
        elif l>=500000 and l<1000000:
            count3+=1
        else:
            count4+=1
    print("=====================Loan Distributaion===============================")
    print(f"0 - 1 lakh: {count1} Customer's")
    print(f"1 - 5 lakh: {count2} Customer's")
    print(f"5 - 10 lakh: {count3} Customer's")
    print(f"10- lakh Above: {count4} Customer's")


def numpyanalyz():
    while True:
        print("""\n----------------- NumPy Analytics -------------------
            =================================================
            1. Salary Statics
            2. Credit Statics")
            3. Count Total Customers")
            4. Display High Risk Customers")
            5. Display High Salary Customers")
            6. Calculate Loan-to-Salary Ratio")
            7. Loan Distribution Analysis")
            8. Back
            =================================================""")
        choice = int(input("Choose Your Option : "))
        if (choice==1):
            salaryStatistics()
        elif(choice==2):
            creditStatistics()
        elif(choice==3):
            countTotalCustomers()
        elif(choice==4):
            displayHighRiskCustomers()
        elif(choice==5):
            displayHighSalaryCustomers()
        elif(choice==6):
            calculateLoanToSalaryRatio()
        elif(choice==7):
            analyzeLoanDistribution()
        elif(choice==8):
            print("Returning to Main Menu...")
            break