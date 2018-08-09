# Import Dependencies 
import os
from pathlib import Path 

# Read file, change between "paragraph_1" or "paragraph_2 below"
txt_file_path =Path("python-challenge", "PyParagraph(Bonus)", "paragraph_3.txt")

# Open file in read mode 
with open(txt_file_path) as text:
    paragraph = text.read()

# Use a list comprehension to split the the text file into words using space as the delimeter and return the appended array "words"
# Obtain length of array 
words = len([w for w in paragraph.split(sep=" ")])

# Use a list comprehension to split the text file into sentences by using ".!?" as the delimeters and return the appended array "sentences"
# Obtain length of array 
sentences = len([w for w in paragraph if w is "."]) + len([w for w in paragraph if w is "?"]) +  len([w for w in paragraph if w is "!"])

# Calculate the average letters in words with isalpha method
letter_avg_per_word = len([c for c in paragraph if c.isalpha()])/words

# Calculate the average words in sentences 
avg_words_per_sentence = words/sentences

# Print statements to terminal 
print(f"Paragraph Analysis")
print(f"-----------------")
print(f"Approximate Word Count: {words}")
print(f"Approximate Sentence Count: {sentences}")
print(f"Average Letter Count: {letter_avg_per_word}")
print(f"Average Sentence Length: {avg_words_per_sentence}")


# Output files, change output file name if needed 
output_file = Path("python-challenge", "PyParagraph(Bonus)", "paragraph_3_analysis.txt")

with open(output_file,"w") as file:
    
# Write methods to export paragraph analysis
    file.write("\n")
    file.write(f"Paragraph Analysis")
    file.write("\n")
    file.write(f"-----------------")
    file.write("\n")
    file.write(f"Approximate Word Count: {words}")
    file.write("\n")
    file.write(f"Approximate Sentence Count: {sentences}")
    file.write("\n")
    file.write(f"Average Letter Count: {letter_avg_per_word}")
    file.write("\n")
    file.write(f"Average Sentence Length: {avg_words_per_sentence}")



