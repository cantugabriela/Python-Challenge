# import libraries 
import os, csv
from pathlib import Path 

# filepath 
csv_file_path = Path('python-challenge\\PyBank\\budget_data.csv')

#variables
total_months = []
total_profit = []
change_profit = []

    
with open(csv_file_path,newline="", encoding='utf-8') as budget:
    csvreader = csv.reader(budget,delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):
        change_profit.append(total_profit[i+1]-total_profit[i])
    

print(len(total_months))
print(sum(total_profit))
print(sum(change_profit)/len(change_profit))


