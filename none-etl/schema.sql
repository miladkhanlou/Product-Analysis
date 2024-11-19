/****************************************
*             Create database           *
****************************************/
CREATE DATABASE product_analysis;
USE product_analysis;


/****************************************
*             Create Tables             *
****************************************/
-- Create Pricing table:
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    asin VARCHAR(20) NOT NULL,
    upc VARCHAR(12) NOT NULL,
    ean VARCHAR(13),
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    brand VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Pricing Table
CREATE TABLE Pricing (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Sales Data Table
CREATE TABLE Sales_Data (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    sales_rank INT,
    units_sold INT,
    date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
