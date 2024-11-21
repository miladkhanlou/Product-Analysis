# NOTE:
Due to the limited time available and the constraints in setting up access to eBay, Walmart, or Amazon APIs, I have provided the ETL pipeline code, which shows the process for extracting, transforming, and loading data, assuming access to the appropriate datasets from these sources.

# ETL Pipeline for Product Analysis
## Purpose:
This project implements an ETL (Extract, Transform, Load) pipeline to:
1. Extract product information, pricing, and sales data from the eBay API.
2. Transform the data into a structured format that aligns with the database schema.
3. Load the transformed data into a relational database for analytics and reporting.

The pipeline supports dynamic pricing strategies and sales performance analysis using modular, scalable, and efficient table structures.

---

## Table Descriptions:
1. **Products**:
   - Metadata table storing product identifiers (`asin`), `name`, and `category`.
   - Timestamps track when records are created and updated.

2. **Pricing**:
   - Tracks historical pricing trends, including `price`, `currency`, and `date`.
   - Linked to the `Products` table via the `asin` field.

3. **Sales_Data**:
   - Captures sales performance metrics, including `sales_rank` and `units_sold`.
   - Linked to `Products` by the `asin` field.

---

## Setup Instructions:
### 1. Install Dependencies
Install the required Python libraries:
```bash
pip install pandas requests sqlalchemy pymysql
```
### 2. Create the Database Schema
```bash
mysql -u <userName> -p < schema.sql
```
This will:
- Create the Products, Pricing, and Sales_Data tables.
- Define relationships and foreign key constraints.

### 3. Run the ETL Pipeline
Execute the ETL pipeline to extract, transform, and load data:

```bash
python etl_pipeline.py
```

### 4. Test CRUD Operations
Run the following command to test CRUD operations:
```bash
mysql -u <userName> -p < crud_operations.sql
```
This will:
- Insert, update, and delete data in the database.
- Execute select queries to verify data relationships and outputs.

---

## Project Objectives
- Automate the extraction, transformation, and loading of product data from eBay.
- Maintain a relational database for dynamic pricing and sales performance analysis.
- Ensure data integrity and scalability through modular schema design.

---

## Future Expansion
- Inventory Management:
   - Add an inventory table to track stock levels for products.
- Customer Reviews:
   - Integrate a reviews table to analyze sentiment and feedback.
- Enhanced Pricing Analytics:
   - Include promotional pricing and seasonal discounts.
- Regional Metrics:
   - Expand `Sales_Data` to track location-specific trends.

---

## Assumptions and Constraints
- Assumptions:
   - Each product has unique identifiers (asin).
   - Sales trends are updated daily.
- Constraints:
   - Pricing and sales data must reference a valid asin from the Products table.
   - Foreign key relationships ensure referential integrity.
