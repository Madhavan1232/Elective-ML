import pandas as pd
import numpy as np
import os
import sys

filename = input().strip()
filePath = os.path.join(sys.path[0], filename)

order_data_df = pd.read_csv(filePath)

print("Central Tendency Measures of order amounts (₹): ")

order_amounts = order_data_df.loc[order_data_df['order_status'] != 'Cancelled'] ['total_amount']

print(f"Mean: {order_amounts.mean():.2f}")
print(f"Median: {order_amounts.median():.1f}")
print(f"Mode: {order_amounts.mode()[0]}")

print("Summary Statistics of Order Amounts:")
completed_orders_ds = order_data_df.loc[order_data_df['order_status'] == 'Completed', 'total_amount']
print(completed_orders_ds.describe())