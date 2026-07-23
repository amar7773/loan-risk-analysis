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
    df.to_csv(r"Loan\customer.csv",index=True)
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
    if customer_id in customer:
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
# Numpy part Start
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

def displaySalaryHistogram():
    df=pd.read_csv("Loan\customer.csv")
    b=[0,20000,40000,60000,80000,100000]
    plt.hist(df["salary"],bins=b,color="gold",label="Salary",edgecolor="b")
    plt.title("Salary Histogram")
    plt.xlabel("Salary")
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

def riskCountPlot():
    df=pd.read_csv("Loan\customer.csv")
    ax=sns.countplot(x="risk",data=df,palette=["g","r"])
    plt.title("Risk Distribution Analysis", fontsize=18)
    plt.xlabel("Risk/Safe")
    plt.ylabel("Customer's Count")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    for bar in ax.patches:
        h=bar.get_height()
        ax.text(
            bar.get_x()+bar.get_width()/2,
            h,
            int(h),
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )
    plt.show()

def correlationHeatmap():
    df=pd.read_csv("Loan\customer.csv")
    x=df.drop(columns=["customer_id","name","risk"])
    sns.heatmap(x,vmin=0,vmax=10,cmap="Accent",annot=True,fmt=".0f",linewidth=10,linecolor="y")
    sns.set(font_scale=1)
    plt.show()

def salaryRiskViolin():
    df=pd.read_csv("Loan\customer.csv")
    sns.violinplot(x="risk",y="salary",data=df,palette="Accent",inner="quart")
    plt.title("Salary and Risk Analysis")
    plt.xlabel("Risk/Safe")
    plt.ylabel("Salary")
    plt.show() 

def customerPairPlot():
    df=pd.read_csv("Loan\customer.csv")
    sns.pairplot(df,kind="reg",diag_kind="hist",vars=df[["salary","loan","credit","age","exp"]],hue="risk")
    plt.show()

def numpyanalyz():
    while True:
        print("\n----------------- NumPy Analytics -------------------")
        print("1. Salary Statics")
        print("2. Credit Statics")
        print("3. Count Total Customers")
        print("4. Display High Risk Customers")
        print("5. Display High Salary Customers")
        print("6. Calculate Loan-to-Salary Ratio")
        print("7. Loan Distribution Analysis")
        print("8. Back")
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
        else:
            print("You Enterd Wrong Choice")

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

def dataVisualization():
    while True:
        print("\n--------------- Data Visualization(Matplotlib)------------------")
        print("1. Salary Bar Chart")
        print("2. Salary Histogram")
        print("3. Salary vs Loan Scatter Plot")
        print("4. Salary Box Plot")
        print("5. Stem Plot (Credit Score)")
        print("\n--------------- Data Visualization(Seaborn) ------------------")
        print("6. Risk Analysis Bar Plot")
        print("7. Risk Count Plot")
        print("8. Core Realtions Heat Map")
        print("9. Salary Risk Violient Plot")
        print("10.Customer's Pair Plot")
        print("11. Back")
        choice = int(input("Choose Your Option : "))
        if (choice==1):
            displaySalaryBarChart()
        elif(choice==2):
            displaySalaryHistogram()
        elif(choice==3):
             displaySalaryLoanScatterPlot()
        elif(choice==4):
            displaySalaryBoxPlot()
        elif(choice==5):
            displaycreditstemPlot()
        elif(choice==6):
            displayRiskAalysisBarplot()
        elif(choice==7):
            riskCountPlot()
        elif(choice==8):
            correlationHeatmap()
        elif(choice==9):
            salaryRiskViolin()
        elif(choice==10):
            customerPairPlot()
        elif(choice==11):
            print("Returning to Main Menu...")
            break
        else:
            print("You Enter Wrong Choice")

while True:
    print("="*60)
    print("Loan Risk Analysis System")
    print("="*60)
    ("0. Exit")
    print("\n--------------- Customer Management ----------------")
    print("1. Add Customer")
    print("2. View All Customers")
    print("3. Search Customer by ID")
    print("4. Update Customer")
    print("5. Delete Customer")
    print("\n----------------- NumPy Analytics -------------------")
    print("6. Numpy Analysis")
    print("\n---------------- Pandas Analytics -------------------")
    print("7.Pandas Analysis")
    print("\n--------------- Data Visualization(Matplotlib,Seaborn)------------------")
    print("8. Data Visualization")
    print("\n----------------- Export Report's --------------------")
    print("9.Export Report's")
    print("="*60)
    choice=int(input("Enter Your Choice:"))
    if(choice==1):
        addCustomer()
    elif(choice==2):
        showCustomer()
    elif(choice==3):
        searchCustomerById()
    elif(choice==4):
        updateCustomer()
    elif(choice==5):
        deleteCustomer()
    elif(choice==6):
        numpyanalyz()
    elif(choice==7):
        pandaAnalyz()
    elif(choice==8):
        dataVisualization()
    elif(choice==9):
        reportsSaves()
    elif(choice==0):
        print("Exit")
        break
    else:
        print("You Enter Wrong Choice")