import pandas as pd
import os
import sys


filename = input().strip()
path = os.path.join(sys.path[0], filename)
data = pd.read_csv(path)

mumbai_data = data.loc[data['city'] == 'Mumbai' ,[ 'appointment_id' , "service_rating"]]
print("Service ratings for appointments in Mumbai: ")
print(mumbai_data)

print("\n Provider ID and Final Amount of the 10th appointment: ")
print(f"Provider ID: {data.iloc[9]['provider_id']}, Final Amount: {data.iloc[9]['final_amount']}")


completed = data.loc[data['status'] == 'completed']

completed["appointment_date"] = pd.to_datetime(completed["appointment_date"])
completed_sorted = completed.sort_values(by='appointment_date' , ascending=False)

recent_5 = completed_sorted.head(5)[['appointment_date' , 'service_name' ]]

print("Last 5 completed appointments (date & service):")
print(recent_5)