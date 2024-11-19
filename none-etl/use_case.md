## Use Case
The database is designed to:
1. Track product price trends and sales performance.
2. Support dynamic pricing strategies and sales forecasting.
3. Enable insights into daily sales trends and product performance.

**Example Scenario**:
- A retailer uses the database to monitor historical sales data and adjust prices dynamically based on trends in sales rank and pricing history.

---

## Table Structure Justification
1. **Products**:
   - Central table for product metadata (e.g., `asin`, `upc`, `ean`).
   - Modular design ensures easy integration with other datasets.
2. **Pricing**:
   - Stores daily pricing trends for each product.
   - Linked to `Products` by `product_id` for consistency and integrity.
3. **Sales_Data**:
   - Designed for time-series data to track daily sales performance.
   - Includes fields for `sales_rank` and `units_sold` to enable trend analysis.

**Benefits**:
- **Efficiency**: Separating metadata, pricing, and sales data ensures faster query performance and easier updates.
- **Scalability**: New tables (e.g., inventory, reviews) can be added without disrupting the schema.
- **Data Integrity**: Foreign key constraints maintain relationships between tables.

---

## Future Expansion
This schema supports future needs such as:
1. Adding a table for inventory management to track stock levels.
2. Creating a customer reviews table to analyze product sentiment.
3. Expanding `Sales_Data` to include region-specific metrics or seasonal trends.
4. Enhancing the `Pricing` table with promotional pricing or discounts.
