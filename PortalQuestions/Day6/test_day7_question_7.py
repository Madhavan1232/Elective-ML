import pandas as pd
import pymysql

con = pymysql.connect("localhost" ,"rootuser" , "rootuser" , "rootuser")
df = pd.read_sql("Select * from appointments" , con)
print(f"Fetched appointments data with columns: {list(df.columns)}")

if df.isnull().any().any():
    df.fillna(method = 'ffill' , inplace = True)
    print("Missing values detected and filled using forward fill. ")
else:
    print("No missing values detected")

if 'appointment_date' in df.columns:
    df['appointment_date'] = pd.to_datetime(df['appointment_date'])
    print("'appointment_date' converted to datetime format.")
else:
    print("Column 'appointment_date' not found.")
    
old_method = df['payment_method'].copy()
df['payment_method'] = df['payment_method'].replace(['PhonePe', 'gpay', 'Google Pay', 'Paytm'], 'UPI')

if not df['payment_method'].equals(old_method):
    print("Payment methods standardized to 'UPI' where applicable.")
else:
    print("No payment methods needed standardization.")
    
rename_col =  {'appointment_date' : 'date' , 'provider_rating' : 'provider_rating'}
df.rename(rename_col , inplace = True)
print(f"Renamed columns: {rename_col}")

total = len(df)
df = df[df['status'] == 'Completed']
kept = len(df)
print(f"Filtered appointments: kept {kept} completed out of {total} total.")

df = df.sort_values(by = 'final_amount' , ascending=False)
print("Sorted data by 'final_amount' in descending order. ")

print("\nAverage final_amount by city:")
print(df.groupby('city')['final_amount'].mean())

print(f"\nMost used payment method: {df['payment_method'].value_counts().idxmax()}\n")

print("Distribution of provider ratings:")
print(df['provider_rating'].describe())
