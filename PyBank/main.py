# Dependencies
import os, csv
from pathlib import Path 

# Declare file location through pathlib
input_file = Path("python-challenge\\PyBank\\budget_data.csv")
output_file = Path("python-challenge\\PyBank\\Financial_Analysis_Summary.txt")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []

# Create empty dictionaries to look up greatest increase/decrease corresponding months
profit_and_months = {}
profit_and_change = {}
    
# Open the file in the default read mode 
with open(input_file,newline="", encoding="utf-8") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Create an appended the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

        # Store the dictionary with the profit as key and month as value
        profit_and_months[row[1]] = row[0]

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
        # Store the values to the profit and change dictionary 
        # Profit and change is the key and Profit is the value
        profit_and_change[total_profit[i+1]-total_profit[i]]=total_profit[i+1]

# Obtain the max and min of the the montly profit change list
max_increase = max(monthly_profit_change)  
max_decrease = min(monthly_profit_change) 


greatest_increase = profit_and_change[max_increase]
greatest_decrease = profit_and_change[max_decrease]

max_inc = profit_and_months[str(greatest_increase)]
max_dec = profit_and_months[str(greatest_decrease)]

#Print Statements


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {max_inc} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {max_dec} (${(str(max_decrease))})")



#Output files

with open(output_file,"w") as file:
#Some methods
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_inc} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {max_dec} (${(str(max_decrease))})")



