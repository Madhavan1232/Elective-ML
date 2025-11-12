import pandas as pd
import os , sys

size = int(input())
record = []
for i in range(size):
    ID , name , mark = input().split()
    record.append({'ID' : ID , 'Name' : name , 'Marks' : mark})

df = pd.DataFrame(record)
print("Initial DataFrame:")
print(df)

arr = input().split()
df.loc[len(df)] = arr

print("\n After Insertion: ")
print(df)

update = input().split()

df.loc[df['ID'] == update[0] , 'Marks'] = update[1]
print("\n After Update (Marks Updated for ID %s): " %update[0])
print(df)

delete_id = input()
df = df.drop(df.loc[df['ID'] == delete_id].index)

print("\n After Deletion (Record Deleted for ID %s):" %delete_id)
print(df)