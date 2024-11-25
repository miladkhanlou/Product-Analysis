# Use Case and Structure Justification

## 1. Use Case:
The ETL pipeline is designed to:
1. Extract product metadata, pricing, and sales data from the eBay API.
2. Transform the data to match the database schema for consistency and analytics.
3. Load the data into the database for further analysis and reporting.

**Example Scenarios**:
- A retailer uses the database to monitor historical sales data and adjust prices dynamically based on trends in sales rank and pricing history.
- Identify products whose sales rank improved over time (a lower rank is better).
- Monitor how many units of each product were sold daily to identify sales trends.
- Calculate the average price for each product over a period of time.

---

## 2. Table Structure Justification:
1. **Products**:
   - Central table for storing metadata such as `asin`, `name`, and `category`.
   - Timestamps (`created_at`, `updated_at`) help track changes over time.
2. **Pricing**:
   - Tracks daily price trends for products.
   - Linked to `Products` by `asin` for consistency and integrity.
3. **Sales_Data**:
   - Captures time-series sales data, including `sales_rank` and `units_sold`.
   - Enables detailed analysis of sales trends.

** Benefits**:
- **Efficiency**: Separation of metadata, pricing, and sales data ensures faster query execution and easier updates.
- **Scalability**: The modular structure supports new tables like inventory or customer reviews without affecting the core schema.
- **Data Integrity**: Foreign key constraints maintain consistent relationships between tables.

---

## 3. Future Expansion:
This schema is flexible for future enhancements, such as:
1. Adding an inventory table to track stock availability.
2. Integrating customer reviews to analyze product sentiment.
3. Incorporating promotional pricing or discounts into the `Pricing` table.
4. Expanding `Sales_Data` to include regional or seasonal metrics.
