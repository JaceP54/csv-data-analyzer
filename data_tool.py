import pandas as pd
import csv

lb = "==============================================================================="
df = pd.read_csv('expenses.csv')

by_date = df.sort_values(by="Date", ascending=True)

Descriptions = df.sort_values(by="Description", ascending=True)

sorted_df = df.sort_values(by="Amount", ascending=False)

total_spent = df["Amount"].sum().round(2)

by_date.to_csv('daily_summary.csv', index=False)
Descriptions.to_csv('categpry_summary.csv', index=False)

"""print(lb)
print(sorted_df[["Description", "Amount"]])
print(lb)
print(by_date[["Date", "Amount"]])
print(lb)
print(total_spent)"""