import pandas as pd

df = pd.read_csv('expenses.csv')

by_date = df["Date"].sort_values
Amount = df["Amount"]
Descriptions = df["Descriptions"]
print(Descriptions)


""" total_spent = df["Amount"].sum().round(2)

print(df[["Date", "Amount"]])

print(by_date)
print(total_spent) """
