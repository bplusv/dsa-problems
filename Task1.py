"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers = set()

for text in texts:
    calling_number, answering_number = text[0], text[1]
    unique_numbers.add(calling_number)
    unique_numbers.add(answering_number)

for call in calls:
    calling_number, answering_number = call[0], call[1]
    unique_numbers.add(calling_number)
    unique_numbers.add(answering_number)

count = len(unique_numbers)

print(f'There are {count} different telephone numbers in the records.')
