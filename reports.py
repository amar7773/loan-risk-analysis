import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from python_crud import customer

def exportSafeCustomers():
    df=pd.read_csv("Loan\customer.csv")
    safe=df[df["risk"]=="Safe"]
    safe.to_csv("Loan\export_safe.csv",index=False)
    print(safe)

def exportRiskCustomers():
    df=pd.read_csv("Loan\customer.csv")
    risk=df[df["risk"]=="Risk"]
    risk.to_csv("Loan\export_risk.csv",index=False)
    print(risk)

def exportEligibleCustomers():
    df=pd.read_csv("Loan\customer.csv")
    el=df.query("salary>=50000 and credit>=700 and risk=='Safe'")
    el.to_csv("Loan\eligble_customer.csv",index=False)
    print(el)

def reportsSaves():
    while True:
        print("\n---------------- Export Reports ---------------------")
        print("1. Export Safe Customers")
        print("2. Export Risk Customers")
        print("3. Export Eligible Customers")
        print("4. Back")
        choice = int(input("Choose Your Option : "))
        if(choice==1):
            exportSafeCustomers()
        elif(choice==2):
            exportRiskCustomers()
        elif(choice==3):
            exportEligibleCustomers()
        elif(choice==4):
            print("Returning to Main Menu...")
            break
        else:
            print("You Enterd Wrong Choice")
