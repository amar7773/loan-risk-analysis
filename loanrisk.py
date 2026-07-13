import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
customer={}
try:
    with open("Loan\cust_data.json","r")as f:
        customer=json.load(f)
        customer={int(k):v for k,v in customer.items()}
except FileNotFoundError:
    customer={}
def customerData():
    with open("Loan\cust_data.json","w")as f:
        json.dump(customer,f,indent=4)

def saveCsv():
    print("saveCsv() Called")
    df=pd.DataFrame.from_dict(customer,orient="index")
    df.index.name = "customer_id"
    df.to_csv("Loan\customer.csv",index=True)
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
        if credit<500:
            risk="Risk"
        else:
            risk="Safe"
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
def searchCustomer():
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
    if customer_id in customer:
        Newname=input("Entetr Name:")
        Newage=int(input("Enter Age:"))
        Newsalary=int(input("Enter Salary:"))
        Newloan=int(input("Enter Loan Amount:"))
        Newcredit=int(input("Enter Credit Score:"))
        Newexperience=int(input("Enter How Many Year Of Exprience You Have:"))
        customer[customer_id]["name"]=Newname
        customer[customer_id]["age"]=Newage
        customer[customer_id]["salary"]=Newsalary
        customer[customer_id]["loan"]=Newloan
        customer[customer_id]["credit"]=Newcredit
        customer[customer_id]["exp"]=Newexperience
        print("==================Customer Details updated Successfuly!======================")
    else:
         print("No Customer ID Found")
    customerData()
    saveCsv()
def deleteCustomer():
    customer_id=int(input("Enter Customer ID:"))
    if customer_id in customer:
        del customer[customer_id]
        print("Customer Deleted Successfuly!")
    else:
         print("No Customer ID Found")
    customerData()
    saveCsv()
# Numpy part Start
def averageSalary():
    print("=======================Average Salary===================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    salary_c=np.array(salary)
    avg=np.mean(salary_c)
    print("Average Salary Of Customer's:",avg)

def maxLoanAmount():
    print("===================Maxium Loan Amount========================")
    loan=[]
    for customer_id in customer:
        loan.append(customer[customer_id]["loan"])
    max_loan=np.array(loan)
    print("Maxium Loan Amount:",np.max(max_loan))

def minimumCreditScore():
    print("================Minimum Credit Score========================")
    credits=[]
    for customer_id in customer:
        credits.append(customer[customer_id]["credit"])
    credit_score=np.array(credits)
    print("Minimum Credit Score:",np.min(credit_score))

def totalCustomer():
    print("=================Total Customer's=======================")
    total=[]
    for customer_id in customer:
        total.append( customer.keys())
    total_customer=np.array(total)
    print("Total Customer's:",total_customer.size)

def highRiskCustomers():
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
        else:
            print("No Risk Customer's!")

def highSalaryCustomer():
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

def lowSalaryLevelCustomer():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    salaries=np.array(salary)
    low_salary=salaries[salaries<50000]
    if len(low_salary)==0:
        print("No Low Level Salary Customer!")
    else:
        print("Total Low Level Salary Customer:",len(low_salary))
    print("==================================")
    for customer_id in customer:
        if customer[customer_id]["salary"]<50000:
            print("Customer ID:",customer_id)
            print("Customer Name:",customer[customer_id]["name"])
            print("Customer Age:",customer[customer_id]["age"])
            print("Customer Salary:",customer[customer_id]["salary"])
            print("Loan Amount:",customer[customer_id]["loan"])
            print("Credit Score:",customer[customer_id]["credit"])
            print("Experience:",customer[customer_id]["exp"])
            print("==================================")

def loanToSalaryRatio():
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

def stdDeviation():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    std_d=np.array(salary)
    print("Standart Deviation:",np.std(std_d))

def medianmiddle():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    median_s=np.array(salary)
    print("Middle Salary",np.median(median_s))

def salaryPercentaile():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    per_s=np.array(salary)
    per=int(input("Enter Percentaile:"))
    print(f"{per}Percentile Salary :",np.percentile(per_s,per))

def topHighest5():
    loan=[]
    for customer_id in customer:
        loan.append(customer[customer_id]["loan"])
    loans=np.array(loan)
    loans_sort=np.argsort(loans[::-1][:5])
    customer_id=list(customer.keys())
    rank=1
    for i in loans_sort:
        cid=customer_id[i]
        print("Rank :", rank)
        print("Customer ID :", cid)
        print("Customer Name :", customer[cid]["name"])
        print("Customer Age :", customer[cid]["age"])
        print("Customer Salary :", customer[cid]["salary"])
        print("Loan Amount :", customer[cid]["loan"])
        print("Credit Score :", customer[cid]["credit"])
        print("Experience :", customer[cid]["exp"])
        print("Risk :", customer[cid]["risk"])
        print("==========================================")

def top5highestSalary():
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    salaries=np.array(salary)
    top5=np.argsort(salaries[::-1][:5])
    customer_id=list(customer.keys())
    rank=1
    for i in top5:
        cid=customer_id[i]
        print("Rank :", rank)
        print("Customer ID :", cid)
        print("Customer Name :", customer[cid]["name"])
        print("Customer Age :", customer[cid]["age"])
        print("Customer Salary :", customer[cid]["salary"])
        print("Loan Amount :", customer[cid]["loan"])
        print("Credit Score :", customer[cid]["credit"])
        print("Experience :", customer[cid]["exp"])
        print("Risk :", customer[cid]["risk"])
        print("==========================================")

def loanDistAnalysis():
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

# ==========================================Pandas============================================
def customerReport():
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

def salaryAnalysis():
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

def loanAnalysis():
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

def riskAnalysis():
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

def advancedSearch():
    df=pd.read_csv("Loan\customer.csv")
    advance=df.query("salary>=50000 and loan<=40000 and credit>=700 and risk=='safe' ")
    print(advance)

def dataCleaningMenu():
    while True:
        print("========== Data Cleaning ==========")
        print("1. Show Missing Values")
        print("2. Fill Missing Salary")
        print("3. Fill Missing Loan")
        print("4. Replace Risk Values")
        print("5. Remove Duplicate Customers")
        print("6. Remove Missing Rows")
        print("7. Back")
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
        elif(choice==4):
            df["risk"]=df["risk"].replace({
            "Risk":"High Risk",
            "Safe":"Low Risk"
        })
            df.to_csv("Loan\customer.csv",index=False)
            print("Risk values replaced successfully!")
            print(df)
        elif(choice==5):
            df.drop_duplicates()
            df.to_csv("Loan\customer.csv",index=False)
            print("Remove Duplicate's Customer's Successfuly")
            print(df)
        elif (choice==6):
            df.dropna()
            df.to_csv("Loan\customer.csv",index=False)
            print("Remove Missing Row's Successfuly")
            print(df)
        elif(choice==7):
            print("Exit")
        else:
            print("You Entered Wrong Choice")

def exportSafe():
    df=pd.read_csv("Loan\customer.csv")
    safe=df[df["risk"]=="Safe"]
    safe.to_csv("Loan\export_safe.csv",index=False)
    print(safe)

def exportRisk():
    df=pd.read_csv("Loan\customer.csv")
    risk=df[df["risk"]=="Risk"]
    risk.to_csv("Loan\export_risk.csv",index=False)
    print(risk)

def eligbleCustomers():
    df=pd.read_csv("Loan\customer.csv")
    el=df.query("salary>=50000 and credit>=700 and risk=='Safe'")
    el.to_csv("Loan\eligble_customer.csv",index=False)
    print(el)

def salaryBarPlot():
    df=pd.read_csv("Loan\customer.csv")
    plt.figure(figsize=(10,5))
    plt.bar(df["name"],df["salary"],color="r")
    for i in range(len(df["salary"])):
        plt.text(i,df["salary"][i],df["salary"][i])
    plt.xticks(rotation=20)
    plt.xlabel("Customer's Name")
    plt.ylabel("Customer's Salary")
    plt.title("Customer Salary Analysis")
    plt.grid(axis="y")
    plt.savefig("salary_bar_plot.png")
    plt.tight_layout()
    plt.show()

def loanBarplot():
    df=pd.read_csv("Loan\customer.csv")
    plt.figure(figsize=(10,5))
    plt.bar(df["name"],df["loan"],color="r")
    for i in range(len(df["salary"])):
        plt.text(i,df["loan"][i],df["loan"][i])
    plt.xticks(rotation=20)
    plt.xlabel("Customer's Name")
    plt.ylabel("Customer's Loam")
    plt.title("Customer Loan Analysis")
    plt.grid(axis="y")
    plt.savefig("loan_bar_plot.png")
    plt.tight_layout()
    plt.show()

while True:
    print("Loan Risk Calculate......................................")
    print("0.Exit")
    print("1.Add Customer")
    print("2.Show Customer's")
    print("3.Search Customer")
    print("4.Update Customer")
    print("5.Delete Customer")
    print("Numpy part..................................................")
    print("6.Average Salary")
    print("7.Maxium Loan Amount")
    print("8.Minimum Credit Score")
    print("9.Total Customer's")
    print("10.High Risk Customer's")
    print("11.High Level Salary Customer's")
    print("12.Low Level Salary Customer's")
    print("13.Loan to Salary Ratio")
    print("14.Standard Deviation of Salary")
    print("15.Median Salary")
    print("16.Percentile of Salary")
    print("17.Top Five Loans")
    print("18.Top Five Salary")
    print("19.Loan Distribution Analysis")
    print("Pandas Part---------------------------------------------------")
    print("20.Customer Reports")
    print("21.Salary Analysis")
    print("22.Loan Analysis")
    print("23.Risk Analysis")
    print("24.Search Customer")
    print("25.Advanced Search")
    print("26.Data Cleaning")
    print("Export Reports-------------------------------------------------")
    print("27.Safe Customer's")
    print("28.Risk Customer's")
    print("29.Eliglbe Customer's")
    print("Matplotlib Part-------------------------------------------------")
    print("30.Salary Plot Bar")
    print("31.Loan Plot Bar")
    choice=int(input("Enter Your Choice:"))
    if(choice==1):
        addCustomer()
    elif(choice==2):
        showCustomer()
    elif(choice==3):
        searchCustomer()
    elif(choice==4):
        updateCustomer()
    elif(choice==5):
        deleteCustomer()
    elif(choice==6):
        averageSalary()
    elif(choice==7):
        maxLoanAmount()
    elif(choice==8):
        minimumCreditScore()
    elif(choice==9):
        totalCustomer()
    elif(choice==10):
        highRiskCustomers()
    elif(choice==11):
        highSalaryCustomer()
    elif(choice==12):
        lowSalaryLevelCustomer()
    elif(choice==13):
        loanToSalaryRatio()
    elif(choice==14):
        stdDeviation()
    elif(choice==15):
        medianmiddle()
    elif(choice==16):
        salaryPercentaile()
    elif(choice==17):
        topHighest5()
    elif(choice==18):
        top5highestSalary()
    elif(choice==19):
        loanDistAnalysis()
    elif(choice==20):
        customerReport()
    elif(choice==21):
        salaryAnalysis()
    elif(choice==22):
        loanAnalysis()
    elif(choice==23):
        riskAnalysis()
    elif(choice==24):
        searchCustomer()
    elif(choice==25):
        advancedSearch()
    elif(choice==26):
        dataCleaningMenu()
    elif(choice==27):
        exportSafe()
    elif(choice==28):
        exportRisk()
    elif(choice==29):
        eligbleCustomers()
    elif(choice==30):
        salaryBarPlot()
    elif(choice==31):
        loanBarplot()
    elif(choice==0):
        print("Exit")
        break
    else:
        print("You Enter Wrong Choice")