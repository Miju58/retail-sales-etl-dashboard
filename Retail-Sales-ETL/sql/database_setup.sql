CREATE DATABASE retail_etl;
USE retail_etl;

CREATE TABLE sales (
    Order_ID VARCHAR(50),
    Product VARCHAR(255),
    Quantity INT,
    Price FLOAT,
    Revenue FLOAT
);
DROP TABLE sales;
CREATE TABLE sales (
    Order_ID VARCHAR(50),
    Product_Name VARCHAR(255),
    Quantity INT,
    Sales FLOAT,
    Profit FLOAT
);
SELECT * FROM sales;