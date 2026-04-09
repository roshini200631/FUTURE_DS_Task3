import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data

# Load data
df = load_data("data/sales_data.csv")

# -----------------------------
# 1. Total Customers
# -----------------------------
total_customers = df['Customer ID'].nunique()

# -----------------------------
# 2. Customers who placed orders
# -----------------------------
customers_with_orders = df.groupby('Customer ID')['Order ID'].nunique()
active_customers = customers_with_orders.count()

# -----------------------------
# 3. Repeat Customers
# -----------------------------
repeat_customers = customers_with_orders[customers_with_orders > 1].count()

# -----------------------------
# 4. High Value Customers
# -----------------------------
customer_sales = df.groupby('Customer ID')['Sales'].sum()
high_value_customers = customer_sales[customer_sales > 1000].count()

# -----------------------------
# Funnel Data
# -----------------------------
funnel = [
    total_customers,
    active_customers,
    repeat_customers,
    high_value_customers
]

stages = [
    "Total Customers",
    "Active Customers",
    "Repeat Customers",
    "High Value Customers"
]

# -----------------------------
# Funnel Visualization
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(stages, funnel)
plt.title("Customer Funnel Analysis")
plt.xticks(rotation=20)
plt.show()

# -----------------------------
# Conversion Rates
# -----------------------------
print("Conversion Rates:")
print(f"Active Rate: {active_customers/total_customers:.2%}")
print(f"Repeat Rate: {repeat_customers/active_customers:.2%}")
print(f"High Value Rate: {high_value_customers/repeat_customers:.2%}")