/********************************************
*                Insert data                *
********************************************/
INSERT INTO Products (asin, upc, ean, name, category, brand)
VALUES 
('B08N5WRWNW', '012345678901', '4006381333931', 'Wireless Earbuds', 'Electronics', 'BrandA'),
('B08L5VT1KC', '234567890123', '4006381333932', 'Smartphone Case', 'Accessories', 'BrandB'),
('B08T5YTQJ2', '345678901234', '4006381333933', 'Bluetooth Speaker', 'Electronics', 'BrandC');

INSERT INTO Pricing (product_id, price, currency, date)
VALUES 
(1, 49.99, 'USD', '2024-11-15'),
(1, 45.99, 'USD', '2024-11-16'),
(2, 19.99, 'USD', '2024-11-15'),
(2, 17.99, 'USD', '2024-11-16'),
(3, 99.99, 'USD', '2024-11-15');

INSERT INTO Sales_Data (product_id, sales_rank, units_sold, date)
VALUES 
(1, 150, 20, '2024-11-15'),
(1, 145, 25, '2024-11-16'),
(2, 300, 15, '2024-11-15'),
(2, 290, 18, '2024-11-16'),
(3, 100, 50, '2024-11-15');

/********************************************
 *               Update Data               *
********************************************/
-- Update Product name:
SELECT * FROM Products;
UPDATE Products
SET name = 'Wireless Earbuds Pro', updated_at = NOW()
WHERE product_id = 1;

-- Update data, Correct Pricing Error:
SELECT * FROM Pricing;
UPDATE Pricing
SET price = 49.99
WHERE price_id = 1;

-- Delete:
DELETE FROM Products WHERE product_id = 3;


/****************************************************
*                    Select Data                    *
****************************************************/
-- Track Daily Units Sold Over Time:
SELECT P.name, S.date, SUM(S.units_sold) AS daily_sales
FROM Sales_Data S
JOIN Products P ON S.product_id = P.product_id
GROUP BY S.product_id, S.date
ORDER BY S.date DESC;

-- List Products with Decreasing Sales Rank:
SELECT P.name, S.date, S.sales_rank
FROM Sales_Data S
JOIN Products P ON S.product_id = P.product_id
WHERE S.sales_rank < (
    SELECT MAX(SD.sales_rank) 
    FROM Sales_Data SD 
    WHERE SD.product_id = S.product_id
)
ORDER BY S.date DESC;
