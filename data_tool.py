import pandas as pd
import csv

lb = "==============================================================================="
df = pd.read_csv('expenses.csv')

by_date = df.sort_values(by="Date", ascending=True)
by_descriptions = df.sort_values(by="Description", ascending=True)
sorted_df = df.sort_values(by="Amount", ascending=False)

total_spent = df["Amount"].sum().round(2)

by_date.to_csv('daily_summary.csv', index=False)
by_descriptions.to_csv('categpry_summary.csv', index=False)


by_date.to_excel('daily_summary.xlsx', index=False)
by_descriptions.to_excel('categpry_summary.xlsx', index=False)

print(total_spent)