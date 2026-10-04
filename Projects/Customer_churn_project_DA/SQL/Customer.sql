CREATE DATABASE customer_churn;

USE customer_churn;

CREATE TABLE customer_churn (
    customerID VARCHAR(20),
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    PhoneService VARCHAR(20),
    MultipleLines VARCHAR(30),
    InternetService VARCHAR(30),
    OnlineSecurity VARCHAR(30),
    OnlineBackup VARCHAR(30),
    DeviceProtection VARCHAR(30),
    TechSupport VARCHAR(30),
    StreamingTV VARCHAR(30),
    StreamingMovies VARCHAR(30),
    Contract VARCHAR(30),
    PaperlessBilling VARCHAR(10),
    PaymentMethod VARCHAR(50),
    MonthlyCharges DECIMAL(10,2),
    TotalCharges DECIMAL(10,2),
    Churn VARCHAR(10),
    TenureGroup VARCHAR(20)
);

SELECT COUNT(*) AS total_customers
FROM customer_churn;

SELECT COUNT(*) AS total_customers
FROM customer_churn;

-- 1. Total customers
SELECT COUNT(*) AS total_customers
FROM customer_churn;

-- 2. Check churn distribution
SELECT Churn, COUNT(*) AS customer_count
FROM customer_churn
GROUP BY Churn;

-- 3. Check gender distribution
SELECT gender, COUNT(*) AS customer_count
FROM customer_churn
GROUP BY gender;

-- 4. Check contract distribution
SELECT Contract, COUNT(*) AS customer_count
FROM customer_churn
GROUP BY Contract;

-- 5. Check internet service distribution
SELECT InternetService, COUNT(*) AS customer_count
FROM customer_churn
GROUP BY InternetService;

-- 6. Overall churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS retained_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn;


-- 7. Churn rate by contract
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY Contract
ORDER BY churn_rate DESC;


-- 8. Churn rate by internet service
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY InternetService
ORDER BY churn_rate DESC;

-- 9. Churn rate by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;


-- 10. Churn rate by tenure group
SELECT
    TenureGroup,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY TenureGroup
ORDER BY churn_rate DESC;


-- 11. Average charges and tenure by churn
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges,
    ROUND(AVG(tenure), 2) AS avg_tenure
FROM customer_churn
GROUP BY Churn;


-- 12. Top 10 customers by total charges
SELECT
    customerID,
    tenure,
    Contract,
    MonthlyCharges,
    TotalCharges,
    Churn
FROM customer_churn
ORDER BY TotalCharges DESC
LIMIT 10;

-- 13. Churn rate by gender
SELECT
    gender,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY gender
ORDER BY churn_rate DESC;


-- 14. Churn rate by senior citizen
SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY SeniorCitizen
ORDER BY churn_rate DESC;


-- 15. Churn rate by monthly charge category
SELECT
    CASE
        WHEN MonthlyCharges < 40 THEN 'Low Charges'
        WHEN MonthlyCharges < 80 THEN 'Medium Charges'
        ELSE 'High Charges'
    END AS charge_category,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn
GROUP BY charge_category
ORDER BY churn_rate DESC;


-- 16. Customers with high monthly charges and churned
SELECT
    customerID,
    Contract,
    InternetService,
    MonthlyCharges,
    tenure,
    Churn
FROM customer_churn
WHERE MonthlyCharges >= 80
  AND Churn = 'Yes'
ORDER BY MonthlyCharges DESC
LIMIT 20;


-- 17. Overall average values
SELECT
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges,
    ROUND(AVG(tenure), 2) AS avg_tenure
FROM customer_churn;

