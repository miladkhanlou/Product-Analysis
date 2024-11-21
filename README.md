# Product Analysis Project

## Overview
This project focuses on organizing and analyzing product information using unique identifiers such as ASIN, UPC, and EAN. The goal is to design an efficient database structure to capture key product details, pricing trends, historical metrics, and sales performance for actionable analysis. The project employs two complementary approaches to achieve this:

1. **Direct Database Design and Management:**
    * Focuses on schema creation, CRUD operations, and database design to enable efficient data organization and retrieval. This approach ensures optimal table structure for both read and write operations to support real-time and historical data queries.
1. **Dynamic Data Pipeline Integration (ETL Approach):**
    * Implements an automated workflow for extracting, transforming, and loading data into the database, ensuring seamless integration of raw data sources with the structured database.

- **An ERD diagram created in Lucidchart showing the database design with Primary Keys (PKs), Foreign Keys (FKs), and relationships.**
  ![ERD](https://github.com/user-attachments/assets/c168f172-8edf-4952-ac52-cd0434af23c4)

## Note: 
Due to time constraints, API integration was not fully implemented, but the provided code assumes access to datasets.

---

## Project Structure
### 1. **`/Data Pipeline Approach`**
This folder contains the implementation of the ETL pipeline:
- **`schema.sql`**: Defines the database schema for the `Products`, `Pricing`, and `Sales_Data` tables.
- **`crud_operations.sql`**: Provides SQL queries for testing data insertion, updates, deletions, and retrieval.
- **`use_case.md`**: Describes the use case, table structure justification, and future expansion for the ETL approach.
- **`etl_pipeline.py`**: Main ETL pipeline code to extract, transform, and load data.
- **`extract_ebay_data.py`**: Python script to simulate data extraction from an API like eBay.

### 2. **`/Schema-Driven Database Implementation`**
This folder contains the non-ETL implementation:
- **`schema.sql`**: Defines the database schema for the `Products`, `Pricing`, and `Sales_Data` tables.
- **`crud_operations.sql`**: Provides SQL queries for data manipulation and retrieval.
- **`use_case.md`**: Describes the use case, table structure justification, and future expansion for the non-ETL approach.

---

### Features
1. **Database Design:**
    * An Entity-Relationship Diagram (ERD) with at least three interconnected tables, including one for time-series data (daily or monthly) to track trends such as price changes and sales ranks.
    * Optimized table structure for scalability, maintainability, and data integrity.

2. CRUD Operations:
    * Read Operations: Enable querying of current product information, historical trend analysis, and metadata retrieval.
    * Write Operations: Support the addition of new product entries for consistent database updates.

3. Use Case Definition:
    * Example Use Case: Tracking pricing trends, sales rank movements, and inventory levels to identify top-performing products or develop pricing strategies.
    * The chosen table structure supports the use case by ensuring efficient data retrieval, trend analysis, and scalability for growing datasets.

4. ETL Workflow (Optional Bonus):
    * A detailed ETL process diagram demonstrating the flow of data from raw sources through transformations into the database.
    * Explanation of how the ETL supports efficient data processing and aligns with the database design.

---
### Use Cases and Analysis:
#### Products with Decreasing Sales Rank:
Identify products whose sales rank improved over time (a lower rank is better).

|         name         |    date    | sales_rnk  |
|----------------------|------------|------------|
| Wireless Earbuds Pro | 2024-11-16 | 145        |
| smartphone Case      | 2024-11-16 | 290        |


#### Track Daily Units Sold Over Time:
Monitor how many units of each product were sold daily to identify sales trends.

| Name                 | Date       | Daily Sales |
|----------------------|------------|-------------|
| Wireless Earbuds Pro | 2024-11-16 | 25          |
| Wireless Earbuds Pro | 2024-11-15 | 20          |
| Smartphone Case      | 2024-11-16 | 18          |
| Smartphone Case      | 2024-11-15 | 15          |
| Bluetooth Speaker    | 2024-11-15 | 50          |

#### Find Average Price Trends for Each Product:
Calculate the average price for each product over a period of time.

|         name         | avg_price |
|----------------------|-----------|
| Wireless Earbuds Pro |   47.99   |
|  Bluetooth Speaker   | 99.990000 |
