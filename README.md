Project Overview
This Python script automates the process of reading, analyzing, and summarizing financial data from a CSV file. It is designed to help users track and understand their spending patterns over time.

Features
Reads a raw expenses.csv file

Calculates the total amount spent

Generates two summaries:

Total spending per day

Total spending per expense category (description)

Sorts the original data by date, description, and amount

Exports the following:

daily_summary.csv and category_summary.csv

daily_summary.xlsx and category_summary.xlsx

expense_report.xlsx with both summaries as separate sheets

Technologies Used
Python 3

pandas for data manipulation and Excel export

csv module (optional, used behind the scenes via pandas)