CREATE DATABASE AluminiumData;
USE AluminiumData;

CREATE TABLE Aluminium (
    Date DATETIME,
    Price INT,
    Open INT,
    High INT,
    Low INT,
    Volume INT,
    Change_Percentage FLOAT
);

LOAD DATA INFILE '/sandeep/Aluminium_Data.csv'
INTO TABLE Aluminium
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Date, Price, Open, High, Low, Volume, Change_Percentage);

SET GLOBAL local_infile = 1

-- Exploratory Data Analysis (EDA)

select * from Aluminium limit 10;

-- Check Total Records
SELECT COUNT(*) FROM Aluminium;

-- Check for Missing Values
SELECT
    SUM(CASE WHEN Date IS NULL THEN 1 ELSE 0 END) AS Missing_Date,
    SUM(CASE WHEN Price IS NULL THEN 1 ELSE 0 END) AS Missing_Price,
    SUM(CASE WHEN Open IS NULL THEN 1 ELSE 0 END) AS Missing_Open,
    SUM(CASE WHEN High IS NULL THEN 1 ELSE 0 END) AS Missing_High,
    SUM(CASE WHEN Low IS NULL THEN 1 ELSE 0 END) AS Missing_Low,
    SUM(CASE WHEN Volume IS NULL THEN 1 ELSE 0 END) AS Missing_Volume,
    SUM(CASE WHEN Change_Percentage IS NULL THEN 1 ELSE 0 END) AS Missing_Change_Percentage
FROM Aluminium;

-- Basic Statistical Summary

SELECT 
    MIN(Price) AS Min_Price,
    MAX(Price) AS Max_Price,
    AVG(Price) AS Avg_Price,
    STDDEV(Price) AS StdDev_Price
FROM Aluminium;

-- Find Duplicate Records

SELECT Date, COUNT(*) 
FROM Aluminium 
GROUP BY Date 
HAVING COUNT(*) > 1;

-- Identify Trends (Monthly Average Price)
SELECT 
    YEAR(Date) AS Year, 
    MONTH(Date) AS Month, 
    AVG(Price) AS Avg_Monthly_Price
FROM Aluminium
GROUP BY Year, Month
ORDER BY Year, Month;














