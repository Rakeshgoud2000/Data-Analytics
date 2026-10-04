-- LOAN DATA ANALYST PROJECT: SQL ANALYSIS
-- Table name: loan_data

-- 1. Total applications
SELECT COUNT(*) AS total_applications FROM loan_data;

-- 2. Approved and rejected applications
SELECT Loan_Status, COUNT(*) AS applications
FROM loan_data
GROUP BY Loan_Status;

-- 3. Overall approval rate
SELECT ROUND(100.0 * SUM(CASE WHEN Loan_Status='Y' THEN 1 ELSE 0 END)/COUNT(*),2) AS approval_rate
FROM loan_data;

-- 4. Approval rate by credit history
SELECT Credit_History,
       COUNT(*) AS applications,
       ROUND(100.0 * SUM(CASE WHEN Loan_Status='Y' THEN 1 ELSE 0 END)/COUNT(*),2) AS approval_rate
FROM loan_data
GROUP BY Credit_History;

-- 5. Approval rate by property area
SELECT Property_Area,
       COUNT(*) AS applications,
       ROUND(100.0 * SUM(CASE WHEN Loan_Status='Y' THEN 1 ELSE 0 END)/COUNT(*),2) AS approval_rate
FROM loan_data
GROUP BY Property_Area
ORDER BY approval_rate DESC;

-- 6. Average income and loan amount by approval status
SELECT Loan_Status,
       ROUND(AVG(ApplicantIncome),2) AS avg_applicant_income,
       ROUND(AVG(CoapplicantIncome),2) AS avg_coapplicant_income,
       ROUND(AVG(LoanAmount),2) AS avg_loan_amount
FROM loan_data
GROUP BY Loan_Status;

-- 7. Education-wise approval
SELECT Education,
       COUNT(*) AS applications,
       ROUND(100.0 * SUM(CASE WHEN Loan_Status='Y' THEN 1 ELSE 0 END)/COUNT(*),2) AS approval_rate
FROM loan_data
GROUP BY Education;

-- 8. Self-employment-wise approval
SELECT Self_Employed,
       COUNT(*) AS applications,
       ROUND(100.0 * SUM(CASE WHEN Loan_Status='Y' THEN 1 ELSE 0 END)/COUNT(*),2) AS approval_rate
FROM loan_data
GROUP BY Self_Employed;

-- 9. Top 10 highest loan amounts
SELECT Loan_ID, TotalIncome, LoanAmount, Credit_History, Property_Area, Loan_Status
FROM loan_data
ORDER BY LoanAmount DESC
LIMIT 10;

-- 10. High-risk applications: poor credit history and high loan amount
SELECT *
FROM loan_data
WHERE Credit_History=0
  AND LoanAmount >= (SELECT AVG(LoanAmount) FROM loan_data)
ORDER BY LoanAmount DESC;
