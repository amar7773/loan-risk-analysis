import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
def calculateAverageSalary():
    print("=======================Average Salary===================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    salary_c=np.array(salary)
    avg=np.mean(salary_c)
    print("Average Salary Of Customer's:",avg)

def findMaximumLoanAmount():
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

def displayLowSalaryCustomers():
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

def calculateSalaryStdDeviation():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    std_d=np.array(salary)
    print("Standart Deviation:",np.std(std_d))

def  calculateMedianSalary():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    median_s=np.array(salary)
    print("Middle Salary",np.median(median_s))

def calculateSalaryPercentile():
    print("==================================")
    salary=[]
    for customer_id in customer:
        salary.append(customer[customer_id]["salary"])
    per_s=np.array(salary)
    per=int(input("Enter Percentaile:"))
    print(f"{per}Percentile Salary :",np.percentile(per_s,per))

def displayTopFiveLoanCustomers():
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

def displayTopFiveSalaryCustomers():
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

# ==========================================Pandas============================================
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

def  advancedCustomerSearch():
    df=pd.read_csv("Loan\customer.csv")
    advance=df.query("salary>=50000 and loan<=40000 and credit>=700 and risk=='safe' ")
    print(advance)

def manageDataCleaning():
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

# ========================================Matplotlib===================================================

def displaySalaryBarChart():
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

def displayLoanBarChart():
    df=pd.read_csv("Loan\customer.csv")
    plt.figure(figsize=(10,5))
    plt.bar(df["name"],df["loan"],color="r")
    for i in range(len(df["loan"])):
        plt.text(i,df["loan"][i],df["loan"][i])
    plt.xticks(rotation=20)
    plt.xlabel("Customer's Name")
    plt.ylabel("Customer's Loam")
    plt.title("Customer Loan Analysis")
    plt.grid(axis="y")
    plt.savefig("loan_bar_plot.png")
    plt.tight_layout()
    plt.show()

def displaySalaryHistogram():
    df=pd.read_csv("Loan\customer.csv")
    b=[0,20000,40000,60000,80000,100000]
    plt.hist(df["salary"],bins=b,color="gold",label="Salary",edgecolor="b")
    plt.title("Salary Histogram")
    plt.xlabel("Salary")
    plt.ylabel("Number of Customers")
    plt.legend()
    plt.show()

def displayCreditHistogram():
    df=pd.read_csv("Loan\customer.csv")
    b=[400,700,750,800,850,900]
    plt.hist(df["credit"],bins=b,color="r",label="Credit",edgecolor="b")
    plt.title("Credit Histogram")
    plt.xlabel("Credit Score")
    plt.ylabel("Number of Customers")
    plt.legend()
    plt.show()

def displaySalaryLoanScatterPlot():
    df=pd.read_csv("Loan\customer.csv")
    plt.figure(figsize=(8,5))
    plt.scatter(df["salary"],df["loan"],color="r",marker="*",label="Salary",alpha=0.4)
    plt.title("Salary and Loan Graph")
    plt.xlabel("Salary")
    plt.ylabel("Loan")
    plt.grid()
    plt.legend()
    plt.show()

def displaySalaryBoxPlot():
    df=pd.read_csv("Loan\customer.csv")
    plt.figure(figsize=(8,5))
    plt.boxplot(df["salary"],boxprops=dict(color="g"),whiskerprops=dict(color="r"),flierprops=dict(color="y"),showmeans=True,tick_labels=["Salary"])
    plt.title("Salary Box Plot")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

def displaycreditstemPlot():
    df=pd.read_csv("Loan\customer.csv")
    plt.stem(df["name"],df["credit"],linefmt=":",markerfmt="ro",basefmt="g",label="Crdit")
    plt.legend(loc=2)
    plt.title("Credit Score Stem Plot",fontsize=20)
    plt.xlabel("Customer's",fontsize=20)
    plt.ylabel("Credit Score",fontsize=20)
    plt.xticks(rotation=45)
    plt.xticks(rotation=90)
    plt.ylim(df["credit"].min()-20,df["credit"].max()+20)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

# ========================================Seaborn===================================================

def  displaySalaryDistribution():
    df=pd.read_csv("Loan\customer.csv")
    sns.displot(df["salary"],kde=True,rug=True,color="g",legend=True)
    plt.axvline(60000,color="gold")
    plt.show()

def displayLoanDistribution():
    df=pd.read_csv("Loan\customer.csv")
    sns.displot(df["loan"],kde=True,rug=True,color="g",legend=True)
    plt.axvline(500000,color="gold")
    plt.show()

def displayCreditDistribution():
    df=pd.read_csv("Loan\customer.csv")
    sns.displot(df["credit"],kde=True,rug=True,color="g",legend=True)
    plt.axvline(750,color="gold")
    plt.show()

def displayRiskAalysisBarplot():
    df=pd.read_csv("Loan\customer.csv")
    avg=df.groupby("risk")["salary"].mean()
    avg_val=avg.index
    avg_sal=avg.values
    sns.barplot(x=avg_val,y=avg_sal,palette=["r","g"])
    plt.title("Average Salary by Risk Category")
    plt.xlabel("Risk Category")
    plt.ylabel("Average Salary")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    for i in range(len(avg_sal)):
        plt.text(i,avg_sal[i],round(avg_sal[i],2))
    plt.show()

def displaySalaryVsLoan():
    df=pd.read_csv("Loan\customer.csv")
    sns.scatterplot(x="salary",y="loan",data=df,hue="risk",style="risk",s=120)
    plt.title("Salary V/s Loan")
    plt.xlabel("Salary")
    plt.ylabel("Loan")
    plt.show()

while True:
    print("="*60)
    print("          Loan Risk Analysis System")
    print("="*60)
    ("0. Exit")
    print("\n--------------- Customer Management ----------------")
    print("1. Add Customer")
    print("2. View All Customers")
    print("3. Search Customer by ID")
    print("4. Update Customer")
    print("5. Delete Customer")

    print("\n----------------- NumPy Analytics -------------------")
    print("6. Calculate Average Salary")
    print("7. Find Maximum Loan Amount")
    print("8. Find Minimum Credit Score")
    print("9. Count Total Customers")
    print("10. Display High Risk Customers")
    print("11. Display High Salary Customers")
    print("12. Display Low Salary Customers")
    print("13. Calculate Loan-to-Salary Ratio")
    print("14. Salary Standard Deviation")
    print("15. Median Salary")
    print("16. Salary Percentile")
    print("17. Top 5 Loan Customers")
    print("18. Top 5 Salary Customers")
    print("19. Loan Distribution Analysis")
 
    print("\n---------------- Pandas Analytics -------------------")
    print("20. Customer Report")
    print("21. Salary Analysis")
    print("22. Loan Analysis")
    print("23. Risk Analysis")
    print("24. Customer Search")
    print("25. Advanced Customer Search")
    print("26. Data Cleaning")

    print("\n---------------- Export Reports ---------------------")
    print("27. Export Safe Customers")
    print("28. Export Risk Customers")
    print("29. Export Eligible Customers")

    print("\n--------------- Data Visualization(Matplotlib)------------------")
    print("30. Salary Bar Chart")
    print("31. Loan Bar Chart")
    print("32. Salary Histogram")
    print("33. Credit Score Histogram")
    print("34. Salary vs Loan Scatter Plot")
    print("35.Salary Box Plot")
    print("36.Stem Plot (Credit Score)")

    print("\n--------------- Data Visualization(Seaborn) ------------------")
    print("37.Salary Distribution")
    print("38.Loan Distribution")
    print("39.Credit Distribution")
    print("40.Risk Analysis Bar Plot")
    print("41.Salary V/s Loan Scatter Plot (Seaborn)")
    print("="*60)
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
        calculateAverageSalary()
    elif(choice==7):
        findMaximumLoanAmount()
    elif(choice==8):
        minimumCreditScore()
    elif(choice==9):
        countTotalCustomers()
    elif(choice==10):
        displayHighRiskCustomers()
    elif(choice==11):
        displayHighSalaryCustomers()
    elif(choice==12):
         displayLowSalaryCustomers()
    elif(choice==13):
        calculateLoanToSalaryRatio()
    elif(choice==14):
        calculateSalaryStdDeviation()
    elif(choice==15):
        calculateMedianSalary()
    elif(choice==16):
        calculateSalaryPercentile()
    elif(choice==17):
        displayTopFiveLoanCustomers()
    elif(choice==18):
        displayTopFiveSalaryCustomers()
    elif(choice==19):
        analyzeLoanDistribution()
    elif(choice==20):
        generateCustomerReport()
    elif(choice==21):
        analyzeSalary()
    elif(choice==22):
        analyzeLoan()
    elif(choice==23):
        analyzeRisk()
    elif(choice==24):
        searchCustomer()
    elif(choice==25):
        advancedCustomerSearch()
    elif(choice==26):
        manageDataCleaning()
    elif(choice==27):
        exportSafeCustomers()
    elif(choice==28):
        exportRiskCustomers()
    elif(choice==29):
        exportEligibleCustomers()
    elif(choice==30):
        displaySalaryBarChart()
    elif(choice==31):
        displayLoanBarChart()
    elif(choice==32):
        displaySalaryHistogram()
    elif(choice==33):
        displayCreditHistogram()
    elif(choice==34):
        displaySalaryLoanScatterPlot()
    elif(choice==35):
        displaySalaryBoxPlot()
    elif(choice==36):
        displaycreditstemPlot()
    elif(choice==37):
        displaySalaryDistribution()
    elif(choice==38):
        displayLoanDistribution()
    elif(choice==39):
        displayCreditDistribution()
    elif(choice==40):
        displayRiskAalysisBarplot()
    elif (choice==41):
        displaySalaryVsLoan()
    elif(choice==0):
        print("Exit")
        break
    else:
        print("You Enter Wrong Choice")