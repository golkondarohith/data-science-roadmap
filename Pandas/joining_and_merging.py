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


#Inner join
merged_inner = pd.merge(df_customers, df_orders, on="Customer_ID", how="inner")
print("Merged data: \n", merged_inner)

#Outer join
merged_outer = pd.merge(df_customers, df_orders, on="Customer_ID", how="outer")
print("Merged data: \n", merged_outer)

#Left join
merged_left = pd.merge(df_customers, df_orders, on="Customer_ID", how="left")
print("Merged data: \n", merged_left)

#Right join
merged_right = pd.merge(df_customers, df_orders, on="Customer_ID", how="right")
print("Merged data: \n", merged_right)