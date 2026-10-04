# 🏦 Loan Application & Risk Analysis

## 📌 Project Overview

This is an end-to-end **Data Analyst portfolio project** that analyzes loan applications to understand approval patterns, applicant characteristics, income, loan amounts, credit history, and potential risk segments.

The project demonstrates the complete Data Analytics workflow:

**Raw Data → Data Cleaning → Excel → SQL → Python → Power BI → Business Insights → Recommendations**

---

## 🎯 Business Objective

The objective is to analyze loan application data and answer important business questions such as:

- How many loan applications were received?
- What is the overall loan approval rate?
- What factors are associated with loan approval?
- How does credit history affect approval?
- Which property areas have higher approval rates?
- How do applicant income and requested loan amount compare?
- Which applications may require additional risk review?
- What KPIs should management monitor?

---

## 🗂️ Dataset

The project uses a **realistic synthetic loan application dataset** designed for portfolio and learning purposes.

### Main columns

| Column | Description |
|---|---|
| `Loan_ID` | Unique application ID |
| `Gender` | Applicant gender |
| `Married` | Marital status |
| `Dependents` | Number of dependents |
| `Education` | Education level |
| `Self_Employed` | Employment status |
| `ApplicantIncome` | Applicant income |
| `CoapplicantIncome` | Co-applicant income |
| `LoanAmount` | Requested loan amount |
| `Loan_Amount_Term` | Loan term in months |
| `Credit_History` | Credit history indicator |
| `Property_Area` | Property area |
| `Loan_Status` | Approved / Rejected |

---

## 🧹 Data Cleaning

The raw dataset was inspected and transformed before analysis.

### Cleaning steps

- Checked rows and columns
- Checked data types
- Identified missing values
- Handled missing categorical values
- Handled missing numerical values
- Checked data consistency
- Created analytical fields
- Prepared an analysis-ready dataset

### Engineered columns

- `Dependents_Num`
- `TotalIncome`
- `Loan_Status_Label`
- `Approval_Flag`
- `Loan_to_Income_Ratio`
- `Estimated_EMI`

---

# 🛠️ Technologies Used

## 📊 Excel

Used for:

- Initial data exploration
- Data cleaning validation
- KPI calculations
- Group analysis
- Business analysis

## 🗄️ SQL

Used for:

- Data aggregation
- Approval-rate analysis
- Credit-history analysis
- Property-area analysis
- Income analysis
- Risk segmentation
- Top-loan analysis

## 🐍 Python

Libraries:

- **Pandas**
- **NumPy**
- **Matplotlib**

Used for:

- Data analysis
- Data validation
- GroupBy analysis
- Aggregation
- Visualization

## 📈 Power BI

Used for:

- Interactive dashboards
- KPI monitoring
- Applicant analysis
- Credit & risk analysis
- Income and loan analysis
- Business storytelling

## 🧮 DAX

Used to create:

- Total Applications
- Approved Applications
- Rejected Applications
- Approval Rate
- Rejection Rate
- Average Loan Amount
- Average Total Income
- Average Loan-to-Income Ratio
- Average Estimated EMI

---

# 📊 Power BI Dashboard

The planned dashboard contains four pages.

### 1. Executive Overview

Key KPIs:

- Total Applications
- Approved Applications
- Rejected Applications
- Approval Rate
- Average Loan Amount

### 2. Applicant Profile

Analysis of:

- Gender
- Marital status
- Dependents
- Education
- Self-employment
- Income

### 3. Credit & Risk

Analysis of:

- Credit history
- Property area
- Education
- Loan-to-income ratio
- High-risk applications

### 4. Income & Loan Analysis

Analysis of:

- Total income
- Loan amount
- Income vs loan amount
- Estimated EMI
- Loan-to-income ratio

---

# 💡 Key Business Insights

### Credit History

Credit history shows a strong relationship with loan approval in this dataset.

Applicants with stronger credit history have a substantially higher approval rate.

### Income & Loan Amount

Applicant income should be evaluated together with the requested loan amount.

A high requested loan relative to income may represent greater affordability risk.

### Property Area

Approval rates vary across property areas.

These differences can be investigated further to understand customer mix and risk characteristics.

### Risk Segment

Applications combining:

**Poor Credit History + High Loan Amount**

can be considered for additional manual review.

---

# 💼 Business Recommendations

1. Prioritize credit-history verification during the application process.
2. Use loan-to-income ratio as a supplementary affordability indicator.
3. Create an additional review segment for high-loan/weak-credit applications.
4. Monitor approval rates by property area and applicant segment.
5. Use Power BI to continuously monitor important lending KPIs.
6. Investigate unusual changes in approval and rejection rates.

---

# 🔄 Project Workflow

```text
Raw CSV
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Excel Analysis
   ↓
SQL Analysis
   ↓
Python Analysis
   ↓
Power BI Dashboard
   ↓
Business Insights
   ↓
Recommendations
```

---

# 📁 Repository Structure

```text
loan-data-analyst-project/
│
├── data/
│   ├── README.md
│   ├── Loan_Raw_Data.csv
│   └── Loan_Cleaned_Data.csv
│
├── excel/
│   ├── README.md
│   └── Loan_Analysis_Excel.xlsx
│
├── sql/
│   ├── README.md
│   └── Loan_Analysis_SQL.sql
│
├── python/
│   ├── README.md
│   └── loan_analysis.py
│
├── powerbi/
│   ├── README.md
│   ├── PowerBI_DAX_Measures.txt
│   ├── PowerBI_Loan_Theme.json
│   ├── PowerBI_Dashboard_Guide.md
│   └── Loan_Analysis.pbix
│
├── report/
│   ├── README.md
│   └── Loan_Project_Report.pdf
│
└── README.md
```

---

# 📌 Project Deliverables

- ✅ Raw dataset
- ✅ Cleaned dataset
- ✅ Excel analysis
- ✅ SQL queries
- ✅ Python analysis
- ✅ Data visualizations
- ✅ Power BI dashboard
- ✅ DAX measures
- ✅ Business insights
- ✅ Business recommendations
- ✅ Final PDF report

---

# 💼 Resume Project Description

**Loan Application & Risk Analysis | Excel, SQL, Python, Power BI**

> Developed an end-to-end loan analytics project using Excel, SQL, Python and Power BI to analyze application trends, approval rates, applicant profiles, credit history, income and loan characteristics. Cleaned and transformed raw data, created analytical metrics, performed SQL and Python analysis, and
