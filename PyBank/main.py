# import libraries 
import os, csv
from pathlib import Path 

# filepath 
csv_file_path = Path('python-challenge\\Resources\\budget_data.csv')

#variables
total_months = 0 
total_profit = 0
previous_profit = 0
profit_change = 0
profits = []
    
with open(csv_file_path,newline="", encoding='utf-8') as budget:
    csvreader = csv.reader(budget,delimiter=",")   

    for row in csvreader: 
        total_months = total_months + 1
        total_profit = total_profit 
    print(total_months)
    print(total_profit)
    print(total_profit)
