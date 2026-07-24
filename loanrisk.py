import json
from python_crud import *
from numpy_analysis import *
from pandas_analysis import *
from visualizationData import *
from reports import *
from aiboat import *
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
    print("\n----------------- AI ASSISTANT --------------------")
    print("10. AI ASSISTANT")
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
    elif(choice==10):
        aiLoanAssistant()
    elif(choice==0):
        print("Exit")
        break
    else:
        print("You Enter Wrong Choice")