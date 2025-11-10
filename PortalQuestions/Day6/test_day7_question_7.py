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

print(f"Filtered appointments: kept {len(df[df['status'] == 'Completed'])} completed out of {len(df)} total.")


