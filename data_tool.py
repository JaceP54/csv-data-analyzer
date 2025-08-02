import pandas as pd
import csv

df = pd.read_csv('expenses.csv')
by_date = df.sort_values(by="Date", ascending=True)
by_descriptions = df.sort_values(by="Description", ascending=True)
sorted_df = df.sort_values(by="Amount", ascending=False)
daily_summary = df.groupby("Date")["Amount"].sum().reset_index()
category_summary = df.groupby("Description")["Amount"].sum().reset_index()

total_spent = df["Amount"].sum().round(2)

by_date.to_csv('daily_summary.csv', index=False)
by_descriptions.to_csv('category_summary.csv', index=False)


by_date.to_excel('daily_summary.xlsx', index=False)
by_descriptions.to_excel('category_summary.xlsx', index=False)

with pd.ExcelWriter("expense_report.xlsx") as writer:
    daily_summary.to_excel(writer, sheet_name="By Date", index=False)
    category_summary.to_excel(writer, sheet_name="By Category", index=False)

print(total_spent)