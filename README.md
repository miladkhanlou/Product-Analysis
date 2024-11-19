# Product Analysis Project

## Overview
This project focuses on organizing and analyzing product information using identifiers such as ASIN, UPC, and EAN. The goal is to design an efficient database structure to capture product details, pricing trends, and sales performance for analysis. The project is implemented in two approaches. 
1. **Non-ETL Approach**: Direct database schema creation and CRUD operations.
2. **ETL Approach**: Automating data extraction, transformation, and loading using Python.
- **An ERD diagram created in Lucidchart showing the database design with Primary Keys (PKs), Foreign Keys (FKs), and relationships.**
  ![ERD](https://github.com/user-attachments/assets/c168f172-8edf-4952-ac52-cd0434af23c4)

## Note: 
Due to time constraints, API integration was not fully implemented, but the provided code assumes access to datasets.

---

## Project Structure
### 1. **`/etl`**
This folder contains the implementation of the ETL pipeline:
- **`schema.sql`**: Defines the database schema for the `Products`, `Pricing`, and `Sales_Data` tables.
- **`crud_operations.sql`**: Provides SQL queries for testing data insertion, updates, deletions, and retrieval.
- **`use_case.md`**: Describes the use case, table structure justification, and future expansion for the ETL approach.
- **`etl_pipeline.py`**: Main ETL pipeline code to extract, transform, and load data.
- **`extract_ebay_data.py`**: Python script to simulate data extraction from an API like eBay.

### 2. **`/non_etl`**
This folder contains the non-ETL implementation:
- **`schema.sql`**: Defines the database schema for the `Products`, `Pricing`, and `Sales_Data` tables.
- **`crud_operations.sql`**: Provides SQL queries for data manipulation and retrieval.
- **`use_case.md`**: Describes the use case, table structure justification, and future expansion for the non-ETL approach.

---

### Features
* **Common to Both Approaches:**
  * Efficient Table Design:
    * Products: Stores product metadata like ASIN, UPC, and category.
    * Pricing: Tracks historical price trends.
    * Sales_Data: Captures daily sales performance metrics.
  * Scalable Schema: Designed for future expansion to include features like inventory tracking or customer reviews.
* **ETL-Specific:**
  * Pipeline Automation: Automates the extraction, transformation, and loading of product data.
  * Code-First Implementation: ETL pipeline scripts simulate API integration and data processing workflows.

---
### Some Use cases and Analysis:
#### Products with Decreasing Sales Rank:
```
+----------------------+------------+------------+
|         name         |    date    | sales_rnk  |
+----------------------+------------+------------+
| Wireless Earbuds Pro | 2024-11-16 | 145        |
| smartphone Case      | 2024-11-16 | 290        |
+----------------------+------------+------------+
```
#### Track Daily Units Sold Over Time:
```
+----------------------+------------+-------------+
|         name         |    date    | daily_sales |
+----------------------+------------+-------------+
| Wireless Earbuds Pro | 2024-11-16	| 25          |
| Wireless Earbuds Pro | 2024-11-15	| 20          |
| Smartphone Case	     | 2024-11-16	| 18          |
| Smartphone Case	     | 2024-11-15	| 15          |
| Bluetooth Speaker	   | 2024-11-15	| 50          |
+----------------------+------------+-------------+
```
#### Find Average Price Trends for Each Product:
```
+----------------------+-----------+
|         name         | avg_price |
+----------------------+-----------+
| Wireless Earbuds Pro |   47.99   |
|  Bluetooth Speaker   | 99.990000 |
+----------------------+-----------+
```
