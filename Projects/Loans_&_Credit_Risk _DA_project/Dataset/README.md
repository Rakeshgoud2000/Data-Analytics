## Loan_Raw_Data.csv
Original dataset used as the starting point.

Contains:
- Loan_ID
- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area
- Loan_Status

The raw file contains missing values intentionally so the data-cleaning process can be demonstrated.

### Loan_Cleaned_Data.csv
Final analysis-ready dataset.

Additional columns:
- Dependents_Num
- TotalIncome
- Loan_Status_Label
- Approval_Flag
- Loan_to_Income_Ratio
- Estimated_EMI

## Cleaning Performed
- Checked missing values
- Filled categorical missing values using mode
- Filled LoanAmount using median
- Filled Loan_Amount_Term using mode
- Filled Credit_History using mode
- Converted Dependents into a numeric field
- Created TotalIncome
- Created Approval_Flag
- Created Loan-to-Income Ratio
- Created Estimated EMI

## Important Note
The dataset is synthetic and intended for portfolio/learning purposes. It is not confidential bank data.

