import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from python_crud import customer

def displaySalaryBarChart():
    df=pd.read_csv("customer.csv")
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
    df=pd.read_csv("customer.csv")
    b=[0,20000,40000,60000,80000,100000]
    plt.hist(df["salary"],bins=b,color="gold",label="Salary",edgecolor="b")
    plt.title("Salary Histogram")
    plt.xlabel("Salary")
    plt.ylabel("Number of Customers")
    plt.legend()
    plt.show()

def displaySalaryLoanScatterPlot():
    df=pd.read_csv("customer.csv")
    plt.figure(figsize=(8,5))
    plt.scatter(df["salary"],df["loan"],color="r",marker="*",label="Salary",alpha=0.4)
    plt.title("Salary and Loan Graph")
    plt.xlabel("Salary")
    plt.ylabel("Loan")
    plt.grid()
    plt.legend()
    plt.show()

def displaySalaryBoxPlot():
    df=pd.read_csv("customer.csv")
    plt.figure(figsize=(8,5))
    plt.boxplot(df["salary"],boxprops=dict(color="g"),whiskerprops=dict(color="r"),flierprops=dict(color="y"),showmeans=True,tick_labels=["Salary"])
    plt.title("Salary Box Plot")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

def displaycreditstemPlot():
    df=pd.read_csv("customer.csv")
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
    df=pd.read_csv("customer.csv")
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
    df=pd.read_csv("customer.csv")
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
    df=pd.read_csv("customer.csv")
    x=df.drop(columns=["customer_id","name","risk"])
    sns.heatmap(x,vmin=0,vmax=10,cmap="Accent",annot=True,fmt=".0f",linewidth=10,linecolor="y")
    sns.set(font_scale=1)
    plt.show()

def salaryRiskViolin():
    df=pd.read_csv("customer.csv")
    sns.violinplot(x="risk",y="salary",data=df,palette="Accent",inner="quart")
    plt.title("Salary and Risk Analysis")
    plt.xlabel("Risk/Safe")
    plt.ylabel("Salary")
    plt.show() 

def customerPairPlot():
    df=pd.read_csv("customer.csv")
    sns.pairplot(df,kind="reg",diag_kind="hist",vars=df[["salary","loan","credit","age","exp"]],hue="risk")
    plt.show()

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