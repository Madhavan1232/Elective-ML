import pandas as pd
import pymysql

con = pymysql.connect("localhost" ,"rootuser" , "rootuser" , "rootuser")

order_df = pd.read_sql("Select * from Orders" , con)
order_df.fillna(method = 'ffill' , inplace = True)
order_df['order_date'] = pd.to_datetime(order_df['order_date'] , errors = 'raise')
order_df['total_amount'] = order_df['total_amount'].astype(float)
order_df = order_df.rename(columns = {'rating' : 'customer_rating' , 'total_amount' : 'total_bill' } )
order_df = order_df[order_df['order_status'] == 'Completed']

print(f"City spending the most: {order_df.groupby('city_user')['total_bill'].sum().idxmax()}")
print(f"Average bill: {order_df['total_bill'].mean()}")
print(f"Bill range: {order_df['total_bill'].max() - order_df['total_bill'].min()}")
print("Payment preferences:")
print(order_df['payment_method'].value_counts())
print("Avg bill by location and payment:")
pivot_table = pd.pivot_table(order_df , values = 'total_bill' ,
index = 'city_user' , columns = 'payment_method' , aggfunc = 'mean' , fill_value = 0)
print(pivot_table)

print("Most used payment each month: ")
dominant_by_month = pd.pivot_table(order_df, index="yearmonth", columns="payment_method", values="user_id", aggfunc="count", fill_value=0)
print(dominant_by_month.idxmax(axis=1))

print("City sales trend across months: ")
pivot_month_sales = pd.pivot_table(order_df , index = 'yearmonth' , columns = 'city_user' , values = 'total_bill' , aggfunc = 'sum' , fill_value = 0)
print(pivot_month_sales)

print("Best rated cities: ")
print(order_df.groupby('city_user')['customer_rating'].mean().sort_values(ascending = False))
