# import libraries 
import os 
import csv 

# filepath 
filepath = "C:\Users\cantu\Desktop\PythonChallenge\python-challenge\PyBank"
csv_filepath = os.path.join(filepath,"budget_data.csv")

#variables
total_months = 0 
total_profit = 0
previous_profit = 0
profit_change = 0
profits = []
    
with open(csv_filepath,newline="", encoding='utf-8') as budget:
    csvreader = csv.reader(budget,delimiter=",")   

    for row in csvreader: 
        total_months = total_months + 1
        total_profit = total_profit 
    print(total_months)
    print(total_profit)
