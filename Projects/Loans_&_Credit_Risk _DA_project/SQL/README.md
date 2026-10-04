# SQL File
`Loan_Analysis_SQL.sql`

## Analysis Included

1. Total applications
2. Approved vs rejected applications
3. Overall approval rate
4. Approval rate by credit history
5. Approval rate by property area
6. Average income by approval status
7. Average loan amount by approval status
8. Education-wise approval
9. Self-employment-wise approval
10. Top 10 highest loan amounts
11. High-risk applications

## SQL Concepts Demonstrated
- SELECT
- COUNT
- SUM
- AVG
- GROUP BY
- ORDER BY
- CASE
- WHERE
- ROUND
- Subqueries
- Conditional aggregation

## Suggested Database
MySQL

## Table Name
`loan_data`

## Example
```sql
SELECT Loan_Status,
       COUNT(*) AS applications
FROM loan_data
GROUP BY Loan_Status;
```

## Goal
Demonstrate practical SQL analysis skills used by Data Analysts when working with business databases.

