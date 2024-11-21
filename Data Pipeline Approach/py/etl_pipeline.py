import pandas as pd
from sqlalchemy import create_engine
import os
from extract_ebay_data import extract_products, extract_pricing, extract_sales

# Database connection
engine = create_engine("mysql+pymysql://MyUserName:MyPassword@localhost/product_analysis")

# Ensure transformed directory exists
os.makedirs('transformed', exist_ok=True)

# --- Transform ---
def transform_products(products_df):
    products_df.rename(columns={"itemId": "asin", "title": "name", "categoryPath": "category"}, inplace=True)
    products_df["created_at"] = pd.Timestamp.now()
    products_df["updated_at"] = pd.Timestamp.now()
    products_df = products_df[["asin", "name", "category", "created_at", "updated_at"]]
    products_df.to_csv("transformed/products_clean.csv", index=False)
    return products_df

def transform_pricing(pricing_df):
    pricing_df.to_csv("transformed/pricing_clean.csv", index=False)
    return pricing_df

def transform_sales(sales_df):
    sales_df.to_csv("transformed/sales_clean.csv", index=False)
    return sales_df

# --- Load ---
def load_to_database(df, table_name):
    df.to_sql(table_name, con=engine, if_exists="append", index=False)

# --- ETL Pipeline ---
def etl_pipeline(query):
    products_df = extract_products(query)
    if products_df is not None:
        clean_products = transform_products(products_df)
        pricing_df = extract_pricing(products_df)
        clean_pricing = transform_pricing(pricing_df)
        sales_df = extract_sales(products_df)
        clean_sales = transform_sales(sales_df)
        load_to_database(clean_products, "Products")
        load_to_database(clean_pricing, "Pricing")
        load_to_database(clean_sales, "Sales_Data")

if __name__ == "__main__":
    etl_pipeline("headphones")
