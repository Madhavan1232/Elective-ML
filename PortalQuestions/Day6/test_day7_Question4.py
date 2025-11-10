import pandas as pd
import pymysql

con = pymysql.connect("localhost" ,"rootuser" , "rootuser" , "rootuser")

df = pd.read_sql("Select * from Orders" , con)
df['order_date'] = pd.to_datetime(df['order_date'] , errors = 'coerce')
df['total_amount'] = df['total_amount'].astype(float)
df.rename(columns = {'total_amount' : 'total_bill'} , inplace = True)

pivot_total = pd.pivot_table(df , index = 'yearmonth' , 
columns = 'payment_method' , values = 'total_bill' , aggfunc = 'sum',fill_value = 0)
print("Total Revenue by Payment Method Across Months: ")
print(pivot_total)

print("\nNumber of Orders at Each Restaurant Every Month: ")
pivot_rs = pd.pivot_table(df , index = 'yearmonth' , columns = 'name_restaurant' 
        , values = 'order_id' , aggfunc = 'count' , fill_value = 0
)
print(pivot_rs)

if 'cuisine_type' not in df.columns:
    print("'cuisine_type' column not found in the data.")