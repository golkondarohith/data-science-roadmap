import pandas as pd


#Region1 details
df_region1 = pd.DataFrame(
    {
        "Customer_ID": [1, 2, 3],
        "Name": ["Raji", "Harsha", "Kethan"]
    }
)

#Region2 details
df_region2 = pd.DataFrame(
    {
        "Customer_ID": [4, 5, 6],
        "Name": ["Akash", "Subbu", "Ram"]
    }
)

#Vertically
df_vstack = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print("Concatenated Verticallay: \n", df_vstack)


#Horizontally
df_hstack = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print("Concatenated Horizontally: \n", df_hstack)