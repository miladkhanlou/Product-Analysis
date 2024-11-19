## The purpose of the project:
This project focuses on organizing and analyzing product information based on identifiers like ASIN, UPC, and EAN. The database tracks product metadata, historical price trends, and sales performance to support dynamic pricing strategies and sales forecasting.

## Table descriptions: 
1. **Products**:
   - Stores metadata about products such as `asin`, `upc`, `ean`, `name`, `category`, and `brand`.
   - Includes timestamps for `created_at` and `updated_at` to maintain record history.

2. **Pricing**:
   - Tracks historical price trends for products.
   - Contains fields for `price`, `currency`, and `date` to record daily or monthly pricing changes.

3. **Sales_Data**:
   - Stores performance metrics like `sales_rank`, `units_sold`, and `date` for products.
   - Designed to handle time-series data for daily sales trends.

---

## Setup Instructions
### 1. Create the Database Schema
Run the following command to set up the database schema:
```bash
mysql -u <UserName> -p < schema.sql
```
This script will:
- Create the product_analysis database.
- Create the Products, Pricing, and Sales_Data tables.
- Define relationships between the tables with foreign key constraints.

### 2. Test CRUD operations:
Run the following command to test CRUD operations:
```bash
mysql -u <UserName> -p < crud_operations.sql
```
This script will:
- Insert sample data into the Products, Pricing, and Sales_Data tables.
- Execute SELECT queries to analyze sales trends and pricing changes.
- Perform UPDATE and DELETE operations to demonstrate data manipulation and integrity.

---

## Project Objectives
- Organize and analyze product information with identifiers like ASIN, UPC, and EAN.
- Enable insights into price trends, sales performance, and dynamic pricing strategies.
- Maintain data integrity and scalability through modular table design.

---

## Assumptions and Constraints
Assumptions:
Each product has unique identifiers (asin, upc, and ean).
Sales trends are recorded daily.
Constraints:
Foreign key relationships ensure referential integrity between tables.
Pricing data must have a valid product_id to maintain integrity.

