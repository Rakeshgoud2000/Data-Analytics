import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Loan_Cleaned_Data.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isna().sum())
print("\nApproval distribution:\n", df["Loan_Status_Label"].value_counts())

print("\nApproval by Credit History:")
print(df.groupby("Credit_History")["Approval_Flag"].mean().mul(100))

print("\nApproval by Property Area:")
print(df.groupby("Property_Area")["Approval_Flag"].mean().mul(100))

print("\nApproval by Education:")
print(df.groupby("Education")["Approval_Flag"].mean().mul(100))

# Example visual
df["Loan_Status_Label"].value_counts().plot(kind="bar")
plt.title("Loan Approval Status")
plt.ylabel("Applications")
plt.show()
