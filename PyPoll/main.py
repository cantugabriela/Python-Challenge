# Import libraries 
import os, csv
from pathlib import Path 

#Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
# Assign file location with the pathlib library
csv_file_path = Path("python-challenge\\PyPoll\\election_data.csv")

# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding='utf-8') as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    #Skip the header so we iterate through the actual values
    header = next(csvreader)     
    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes = total_votes + 1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li": 
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

    # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]


# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis

print(total_votes)
print(khan_votes)
print(((khan_votes/total_votes)*100))
print(correy_votes)
print((correy_votes/total_votes)*100)
print(li_votes)
print((li_votes/total_votes)*100)
print(otooley_votes)
print((otooley_votes/total_votes)*100)
print(key)
