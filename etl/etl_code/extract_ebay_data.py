import requests
import pandas as pd
import os

# staging directory
os.makedirs('staging', exist_ok=True)

# eBay API credentials
APP_ID = "APP_ID"
AUTH_TOKEN = "TOKEN"

# Base URL for eBay API
BASE_URL = "https://api.ebay.com/buy/browse/v1/item_summary/search"

# Function to extract product data
def extract_products(query, limit=10):
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
    }
    params = {
        "q": query,
        "limit": limit,
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        with open("staging/products_raw.json", "w") as f:
            f.write(response.text)
        return pd.json_normalize(data.get("itemSummaries", []))
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
# Function to extract pricing data
def extract_pricing(products_df):
    pricing_data = products_df[["itemId", "price.value", "price.currency"]].copy()
    pricing_data.rename(columns={
        "itemId": "asin",
        "price.value": "price",
        "price.currency": "currency"
    }, inplace=True)
    pricing_data["date"] = pd.Timestamp.now()
    pricing_data.to_json("staging/pricing_raw.json", orient="records")
    return pricing_data

# Function to extract sales data
def extract_sales(products_df):
    sales_data = products_df[["itemId", "title", "categoryPath", "condition"]].copy()
    sales_data.rename(columns={
        "itemId": "asin",
        "title": "name",
        "categoryPath": "category",
        "condition": "condition"
    }, inplace=True)
    sales_data["sales_rank"] = 0  # Placeholder, as eBay doesn’t provide direct rank
    sales_data["units_sold"] = 0  # Placeholder
    sales_data["date"] = pd.Timestamp.now()
    sales_data.to_json("staging/sales_raw.json", orient="records")
    return sales_data

if __name__ == "__main__":
    products_df = extract_products("headphones")
    if products_df is not None:
        pricing_df = extract_pricing(products_df)
        sales_df = extract_sales(products_df)
