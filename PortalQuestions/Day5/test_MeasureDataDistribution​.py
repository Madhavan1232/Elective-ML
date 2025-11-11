import pandas as pd
import numpy as np
import os
import sys
from scipy.stats import skew, kurtosis

path = os.path.join(sys.path[0], input())
df = pd.read_csv(path)
    
completed_orders = df[df['order_status'] == 'Completed']

amount_range = completed_orders['total_amount'].max() - completed_orders['total_amount'].min()
variance = completed_orders['total_amount'].var()
std_deviation = completed_orders['total_amount'].std()
print("--- Spread / Dispersion ---")
print("Range:", amount_range)
print("Variance:", variance.round(2))
print("Standard Deviation:", std_deviation.round(2))

skewness_val = skew(completed_orders['total_amount'])
kurtosis_val = kurtosis(completed_orders['total_amount'])

print("\n--- Distribution Shape ---")
print(f"Skewness: {round(skewness_val , 3)}")
print(f"Kurtosis: {round(kurtosis_val , 3)}")

print("\n--- Insights ---")
print("- Range shows the spread between the smallest and largest order amounts.")
print("- High variance or standard deviation indicates variability in order amounts.")
if skewness_val > 0:
    print("- Positive skewness: distribution has a long tail to the right (some very high orders).")
elif skewness_val < -0.1:
    print("- Negative skewness: distribution has a long tail to the left (some very low orders).")
else:
    print("- Skewness near 0: distribution is roughly symmetric.")
if kurtosis_val > 0.1:
    print("- Positive kurtosis: sharper peak and fatter tails than a normal distribution.")
elif kurtosis_val < -0.1:
    print("- Negative kurtosis: flatter distribution than normal.")
else:
    print("- Kurtosis near 0: distribution is similar to a normal distribution.")