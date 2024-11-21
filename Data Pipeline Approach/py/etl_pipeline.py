
import requests
import pandas as pd
from sqlalchemy import create_engine
from pprint import pprint
import json
import os

# API Configuration
BASE_URL = "https://api.keepa.com"
API_KEY = "YOUR_API_KEY"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Directory to save raw JSON files
output_dir = "raw_json_files"
os.makedirs(output_dir, exist_ok=True)

# Endpoints for data extraction (replace with actual endpoints)
endpoints = {
    "product": f"{BASE_URL}/product",
    "seller": f"{BASE_URL}/seller",
    "bestsellers": f"{BASE_URL}/bestsellers"
}

# Data extraction
def extract_data():
    for endpoint_name, url in endpoints.items():
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            with open(f"{output_dir}/{endpoint_name}.json", "w") as f:
                json.dump(response.json(), f)
        else:
            print(f"Failed to fetch data from {endpoint_name} - {response.status_code}")

# Transformation functions
def transform_product_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [
        {
            "ASIN": product["asin"],
            "Title": product["title"],
            "Price (Amazon)": product.get("csv", {}).get("AMAZON", [None])[-1],
            "Rank": product.get("salesRanks", {}).get("categoryId", None),
            "Reviews": product.get("csv", {}).get("COUNT_REVIEWS", [None])[-1],
            "Variations": ", ".join([v.get("attribute", "") for v in product.get("variations", [])]),
        }
        for product in data["products"]
    ]

#Price History CSV
def transform_price_history(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [
        {
            "ASIN": product["asin"],
            "Price History (Amazon)": product.get("csv", {}).get("AMAZON", []),
            "Timestamps": product.get("csv_time", [])
        }
        for product in data["products"]
    ]

#Sales Rank History CSV
def transform_sales_rank_history(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [
        {
            "ASIN": product["asin"],
            "Sales Rank History": product.get("salesRanks", {}),
            "Timestamps": product.get("salesRanks_time", []),
        }
        for product in data["products"]
    ]


#Seller Data CSV
def transform_seller_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [
        {
            "Seller ID": seller["sellerId"],
            "Rating": seller["rating"],
            "ASINs Sold": ", ".join(seller.get("asinList", [])),
        }
        for seller in data["sellers"].values()
    ]


#Category/Subcategory CSV
def transform_category_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [
        {
            "Category ID": category["categoryId"],
            "Category Name": category.get("name"),
            "Parent Category ID": category.get("parent", None),
        }
        for category in data["bestSellersList"]
    ]


# Database connection
engine = create_engine("mysql+pymysql://MyUserName:MyPassword@localhost/product_analysis")

def load_to_database(df, table_name):
    df.to_sql(table_name, con=engine, if_exists="append", index=False)

def etl_pipeline():
    # Extraction logic
    extract_data()

    # Transformation logic
    product_data = transform_product_data("raw_json_files/products.json")
    price_history = transform_price_history("raw_json_files/price_history.json")
    sales_rank = transform_sales_rank_history("raw_json_files/sales_rank.json")
    seller_data = transform_seller_data("raw_json_files/sellers.json")
    category_data = transform_category_data("raw_json_files/categories.json")
    
    # Save to staging Location:
    pd.DataFrame(product_data).to_csv("products.csv", index=False)
    pd.DataFrame(price_history).to_csv("price_history.csv", index=False)
    pd.DataFrame(sales_rank).to_csv("sales_rank.csv", index=False)
    pd.DataFrame(seller_data).to_csv("sellers.csv", index=False)
    pd.DataFrame(category_data).to_csv("categories.csv", index=False)
    
    # Load logic
    load_to_database(product_data, "Products")
    load_to_database(price_history, "Pricing")
    load_to_database(sales_rank, "Sales_Rank")
    load_to_database(seller_data, "Sellers")
    load_to_database(category_data, "Categories")

if __name__ == "__main__":
    etl_pipeline()



