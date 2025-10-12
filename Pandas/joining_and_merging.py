import pandas as pd


#Customer details
df_customers = pd.DataFrame(
    {
        "Customer_ID": [1, 2, 3],
        "Name": ["Raji", "Harsha", "Kethan"]
    }
)

#Order details
df_orders = pd.DataFrame(
    {
        "Customer_ID": [1, 2, 4],
        "OrderAmount": [250, 500, 123]
    }
)

merged = pd.merge(df_customers, df_orders, on="Customer_ID", how="inner")
print("Merged data: \n", merged)