# 🏦 AI Loan Risk Analysis & Prediction System

An end-to-end **AI-based Loan Risk Analysis and Prediction System** developed using Python, NumPy, Pandas, Machine Learning, NLP, and FastAPI.

The system can manage customer data, perform statistical analysis, predict loan risk, understand user queries using NLP, and expose AI models through REST APIs.

---

## 📌 Features

### 🐍 Python / CRUD
- Add Customer
- Show Customer
- Search Customer
- Update Customer
- Delete Customer
- JSON File Handling
- Customer Data Management

---

### 📊 NumPy
- Average Salary
- Maximum Loan
- Minimum Credit Score
- Total Customers
- High Risk Customers
- High Salary Customers
- Low Salary Customers
- Loan to Salary Ratio
- Standard Deviation
- Median Salary
- Percentile Analysis
- Top 5 Highest Loan Customers
- Top 5 Highest Salary Customers
- Loan Distribution Analysis

---

### 🐼 Pandas
- Customer Report
- Salary Analysis
- Loan Analysis
- Risk Analysis
- Customer Search & Filter
- Advanced Search
- Export Safe Customers
- Export Risk Customers
- Export Eligible Customers
- CSV Data Processing

---

# 🤖 Machine Learning

The project uses Machine Learning to predict whether a customer is **Safe** or **High Risk** for a loan.

### Features Used

- Age
- Salary
- Loan Amount
- Credit Score
- Experience

### Models Compared

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Naive Bayes
- Support Vector Machine
- Gradient Boosting

### Model Evaluation

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Cross Validation

### Hyperparameter Tuning

Used `GridSearchCV` to find better parameters for the Logistic Regression model.

### Model Saving

Models are saved using Joblib:

```text
loan_risk_model.pkl
loan_scaler.pkl
risk_encoder.pkl