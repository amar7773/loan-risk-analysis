import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
customer={}
try:
    with open("cust_data.json","r")as f:
        customer=json.load(f)
        customer={int(k):v for k,v in customer.items()}
except FileNotFoundError:
    customer={}
def customerData():
    with open("cust_data.json","w")as f:
        json.dump(customer,f,indent=4)

def saveCsv():
    print("saveCsv() Called")
    df=pd.DataFrame.from_dict(customer,orient="index")
    df.index.name = "customer_id"
    df.to_csv(r"customer.csv",index=True)
    print("CSV Saved")
    
def addCustomer():
    customer_id=int(input("Enter Customer ID:"))
    if customer_id in customer:
        print("Customer Already Added!")
    else:
        name=input("Entet Name:")
        age=int(input("Enter Age:"))
        salary=int(input("Enter Salary:"))
        loan=int(input("Enter Loan Amount:"))
        credit=int(input("Enter Credit Score:"))
        experience=int(input("Enter How Many Year Of Exprience You Have:"))
        if salary>=50000 and credit>=700 and experience>=2 and loan<=salary*5:
            risk="Safe"
        else:
            risk="Risk"
        customer[customer_id]={
            "name":name,
            "age":age,
            "salary":salary,
            "loan":loan,
            "credit":credit,
            "exp":experience,
            "risk":risk
            }
        print("Customer Added Successfuly!")
        customerData()
        saveCsv()
def showCustomer():
    if len(customer) == 0:
        print("No Customer Found")
    else:
        for customer_id in customer:
            print("===============================Details of All Customer's====================================")
            print("Customer ID:",customer_id)
            print("Customer Name:",customer[customer_id]["name"])
            print("Customer Age:",customer[customer_id]["age"])
            print("Customer Salary:",customer[customer_id]["salary"])
            print("Loan Amount:",customer[customer_id]["loan"])
            print("Credit Score:",customer[customer_id]["credit"])
            print("Experience:",customer[customer_id]["exp"])
            print("Risk:",customer[customer_id]["risk"])
            customerData()
def searchCustomerById():
    print("===================Details of Search Customer==========================")
    customer_id=int(input("Enter Customer ID:"))
    if customer_id in customer:
        print("Customer ID:",customer_id)
        print("Customer Name:",customer[customer_id]["name"])
        print("Customer Age:",customer[customer_id]["age"])
        print("Customer Salary:",customer[customer_id]["salary"])
        print("Loan Amount:",customer[customer_id]["loan"])
        print("Credit Score:",customer[customer_id]["credit"])
        print("Experience:",customer[customer_id]["exp"])
        print("Risk:",customer[customer_id]["risk"])
    else:
        print("No Customer ID Found")
    customerData()
def updateCustomer():
    customer_id=int(input("Enter Customer ID:"))
    print("Entered ID:", customer_id)
    print("All IDs:", list(customer.keys()))
    print("Exists:", customer_id in customer)
    if customer_id in customer:
        while True:
            print("""
            ==============================
      UPDATE CUSTOMER
      ==============================
      1. Update All Details
      2. Update Customer Name
      3. Update Customer Age
      4. Update Salary
      5. Update Loan
      6. Update Credit
      7. Update Experience
      8. Back
      ==============================
      """)
            choice=int(input("Choose a Options:"))
            if(choice==1):
                Newname=input("Entetr Name:")
                Newage=int(input("Enter Age:"))
                Newsalary=int(input("Enter Salary:"))
                Newloan=int(input("Enter Loan Amount:"))
                Newcredit=int(input("Enter Credit Score:"))
                Newexperience=int(input("Enter How Many Year Of Exprience You Have:"))
                if Newcredit < 500 or Newloan > Newsalary * 10:
                    risk = "Risk"
                else:
                    risk = "Safe"
                customer[customer_id]["name"]=Newname
                customer[customer_id]["age"]=Newage
                customer[customer_id]["salary"]=Newsalary
                customer[customer_id]["loan"]=Newloan
                customer[customer_id]["credit"]=Newcredit
                customer[customer_id]["exp"]=Newexperience
                customer[customer_id]["risk"]=risk
                print("==================Customer Details updated Successfuly!======================")
                customerData()
                saveCsv()
                print("Customer Updated Successfully!")
            elif(choice==2):
                print("Current Name:",customer[customer_id]["name"])
                Newname=input("Entetr Name:")
                customer[customer_id]["name"]=Newname
                customerData()
                saveCsv()
            elif(choice==3):
                print("Current Age:",customer[customer_id]["age"])
                Newage=int(input("Enter Age:"))
                customer[customer_id]["age"]=Newage
                customerData()
                saveCsv()
            elif(choice==4):
                print("Current Salary:",customer[customer_id]["salary"])
                Newsalary=int(input("Enter Salary:"))
                customer[customer_id]["salary"]=Newsalary
                if customer[customer_id]["credit"] < 500 or customer[customer_id]["loan"] > Newsalary * 10:
                    risk = "Risk"
                else:
                    risk = "Safe"
                customer[customer_id]["risk"] = risk
                customerData()
                saveCsv()
            elif(choice==5):
                print("Current Loan:",customer[customer_id]["loan"])
                Newloan=int(input("Enter Loan Amount:"))
                customer[customer_id]["loan"]=Newloan
                if customer[customer_id]["credit"]  < 500 or Newloan > customer[customer_id]["salary"] * 10:
                    risk = "Risk"
                else:
                    risk = "Safe"
                customer[customer_id]["risk"] = risk
                customerData()
                saveCsv()
            elif(choice==6):
                print("Current Credit:",customer[customer_id]["credit"])
                Newcredit=int(input("Enter Credit Score:"))
                customer[customer_id]["credit"]=Newcredit
                if  Newcredit < 500 or customer[customer_id]["loan"] > customer[customer_id]["salary"] * 10:
                    risk = "Risk"
                else:
                    risk = "Safe"
                customer[customer_id]["risk"] = risk
                customerData()
                saveCsv()
            elif(choice==7):
                print("Current Experience:",customer[customer_id]["exp"])
                Newexperience=int(input("Enter How Many Year Of Exprience You Have:"))
                customer[customer_id]["exp"]=Newexperience
                customerData()
                saveCsv()
            elif(choice==8):
                print("Back")
                break
            else:
                print("You Enter Wrong Choice")
    else:
         print("No Customer ID Found")
def deleteCustomer():
    customer_id=int(input("Enter Customer ID:"))
    if customer_id in customer:
        del customer[customer_id]
        customerData()
        saveCsv()
        print("Customer Deleted Successfuly!")
    else:
         print("No Customer ID Found")
