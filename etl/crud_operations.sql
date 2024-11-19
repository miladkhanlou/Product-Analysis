/********************************************
*                Insert data                *
********************************************/
-- Insert a product
INSERT INTO Products (asin, name, category)
VALUES ('B08XYZ1234', 'Wireless Headphones', 'Electronics');

-- Insert pricing data
INSERT INTO Pricing (asin, price, currency, date)
VALUES ('B08XYZ1234', 49.99, 'USD', '2024-11-18');

-- Insert sales data
INSERT INTO Sales_Data (asin, name, category, sales_rank, units_sold, date)
VALUES ('B08XYZ1234', 'Wireless Headphones', 'Electronics', 100, 50, '2024-11-18');

/*******************************************
 *               Update Data               *
 ********************************************/
-- Update the price of a product
SELECT * FROM Pricing;
UPDATE Pricing
SET price = 59.99
WHERE asin = 'B08XYZ1234';

/********************************************
*                  Delete                   *
********************************************/
-- Remove a product and related data
DELETE FROM Products WHERE asin = 'B08XYZ1234';

/****************************************************
*                    Select Data                    *
****************************************************/
-- Retrieve product details with pricing
SELECT p.asin, p.name, pr.price, pr.currency
FROM Products p
JOIN Pricing pr ON p.asin = pr.asin;

-- Retrieve sales trends
SELECT s.asin, s.name, s.sales_rank, s.units_sold, s.date
FROM Sales_Data s
ORDER BY s.date DESC;
