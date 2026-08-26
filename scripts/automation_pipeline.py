import pandas as pd
import os

# 1. Load raw data
raw_file = "Superstore sales dataset.csv"
data = pd.read_csv(raw_file)

print("Raw data loaded successfully!")

# 2. Clean data
data = data.drop_duplicates()
data = data.dropna()

print("Data cleaning completed!")

# 3. Calculate KPIs
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_quantity = data["Quantity"].sum()
total_orders = data["Order ID"].nunique()

# 4. Create KPI report
kpi_report = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Profit",
        "Total Quantity",
        "Total Orders"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_quantity,
        total_orders
    ]
})

# 5. Save processed data
data.to_csv("Superstore_processed.csv", index=False)

# 6. Export results to Excel
with pd.ExcelWriter("Task_5_Final_Output.xlsx") as writer:
    data.to_excel(writer, sheet_name="Processed Data", index=False)
    kpi_report.to_excel(writer, sheet_name="KPI Summary", index=False)

print("Processed data saved successfully!")
print("Excel report created successfully!")

print("\nKEY KPIs")
print("=" * 30)
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity:", total_quantity)
print("Total Orders:", total_orders)