import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())

print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].dtype)
print(df["TotalCharges"].isnull().sum())

df["TotalCharges"] = df["TotalCharges"].fillna(0)

print("Missing TotalCharges:", df["TotalCharges"].isnull().sum())

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 60, 72],
    labels=["0-12 Months", "13-24 Months", "25-48 Months", "49-60 Months", "61-72 Months"]
)

print(df[["tenure", "TenureGroup"]].head())
print(df["TenureGroup"].value_counts().sort_index())

print("Dataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================
# PART 3 - DATA ANALYSIS
# ==========================================

# Total Customers
total_customers = df["customerID"].nunique()

# Churned Customers
churned_customers = (df["Churn"] == "Yes").sum()

# Retained Customers
retained_customers = (df["Churn"] == "No").sum()

# Overall Churn Rate
churn_rate = (churned_customers / total_customers) * 100

# Average Monthly Charges
avg_monthly_charges = df["MonthlyCharges"].mean()

# Average Total Charges
avg_total_charges = df["TotalCharges"].mean()

# Average Customer Tenure
avg_tenure = df["tenure"].mean()

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print("Churn Rate:", round(churn_rate, 2), "%")
print("Average Monthly Charges:", round(avg_monthly_charges, 2))
print("Average Total Charges:", round(avg_total_charges, 2))
print("Average Tenure:", round(avg_tenure, 2), "months")

# Customer distribution

print("\nCUSTOMERS BY GENDER")
print(df["gender"].value_counts())

print("\nCUSTOMERS BY CONTRACT")
print(df["Contract"].value_counts())

print("\nCUSTOMERS BY INTERNET SERVICE")
print(df["InternetService"].value_counts())

print("\nCUSTOMERS BY PAYMENT METHOD")
print(df["PaymentMethod"].value_counts())


# Churn rate by category

print("\nCHURN RATE BY GENDER")
print(df.groupby("gender")["Churn"].apply(lambda x: (x == "Yes").mean() * 100))

print("\nCHURN RATE BY CONTRACT")
print(df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean() * 100))

print("\nCHURN RATE BY INTERNET SERVICE")
print(df.groupby("InternetService")["Churn"].apply(lambda x: (x == "Yes").mean() * 100))

print("\nCHURN RATE BY PAYMENT METHOD")
print(df.groupby("PaymentMethod")["Churn"].apply(lambda x: (x == "Yes").mean() * 100))

print("\nCHURN RATE BY SENIOR CITIZEN")
print(df.groupby("SeniorCitizen")["Churn"].apply(lambda x: (x == "Yes").mean() * 100))

print("\nCHURN RATE BY TENURE GROUP")
print(df.groupby("TenureGroup")["Churn"].apply(lambda x: (x == "Yes").mean() * 100))

# Churned vs Retained comparison

print("AVERAGE MONTHLY CHARGES BY CHURN")
print(df.groupby("Churn")["MonthlyCharges"].mean())

print("\nAVERAGE TENURE BY CHURN")
print(df.groupby("Churn")["tenure"].mean())

print("\nAVERAGE TOTAL CHARGES BY CHURN")
print(df.groupby("Churn")["TotalCharges"].mean())


# Top 10 customers by Total Charges

print("\nTOP 10 CUSTOMERS BY TOTAL CHARGES")
print(
    df[["customerID", "TotalCharges", "Churn"]]
    .sort_values("TotalCharges", ascending=False)
    .head(10)
)

# ==========================================
# PART 4 - PYTHON VISUALIZATION
# ==========================================

# 1. Churn Distribution - Pie Chart

churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    churn_counts,
    labels=churn_counts.index,
    autopct="%1.1f%%"
)
plt.title("Customer Churn Distribution")
plt.show()


# 2. Customer Distribution by Contract

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract")
plt.title("Customer Distribution by Contract")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=15)
plt.show()


# 3. Churn by Contract

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Churn by Contract")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=15)
plt.show()


# 4. Churn by Gender

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="gender", hue="Churn")
plt.title("Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.show()

# 5. Churn by Internet Service

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="InternetService", hue="Churn")
plt.title("Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.show()


# 6. Churn by Payment Method

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="PaymentMethod", hue="Churn")
plt.title("Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)
plt.show()


# 7. Tenure Distribution

plt.figure(figsize=(8, 5))
plt.hist(df["tenure"], bins=20)
plt.title("Customer Tenure Distribution")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.show()


# 8. Monthly Charges Distribution

plt.figure(figsize=(8, 5))
plt.hist(df["MonthlyCharges"], bins=20)
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()

# 9. Tenure vs Monthly Charges

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="tenure",
    y="MonthlyCharges",
    hue="Churn"
)
plt.title("Tenure vs Monthly Charges")
plt.xlabel("Tenure (Months)")
plt.ylabel("Monthly Charges")
plt.show()


# 10. Monthly Charges by Churn

plt.figure(figsize=(7, 5))
sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges"
)
plt.title("Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.show()

# 11. Total Charges by Churn

plt.figure(figsize=(7, 5))
sns.boxplot(
    data=df,
    x="Churn",
    y="TotalCharges"
)
plt.title("Total Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Total Charges")
plt.show()

# 12. Churn Rate by Tenure Group

churn_by_tenure = df.groupby("TenureGroup")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

plt.figure(figsize=(9, 5))
churn_by_tenure.plot(kind="bar")
plt.title("Churn Rate by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=20)
plt.show()

# 13. Service Usage

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="InternetService")
plt.title("Service Usage")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.show()

# 14. Correlation Heatmap

numeric_df = df[
    ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]
]

plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()

# ==========================================
# SAVE CLEANED DATASET
# ==========================================
df.to_csv(
    "Customer_Churn_Cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully.")


print(df.shape)