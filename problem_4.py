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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


sends_text_numbers = set()
receives_text_numbers = set()
for text in texts:
    sending_number, receiving_number = text[0], text[1]
    sends_text_numbers.add(sending_number)
    receives_text_numbers.add(receiving_number)

makes_call_numbers = set()
receives_call_numbers = set()
for call in calls:
    calling_number, answering_number = call[0], call[1]
    makes_call_numbers.add(calling_number)
    receives_call_numbers.add(answering_number)

possible_telemarketers = sorted(makes_call_numbers - receives_call_numbers - sends_text_numbers - receives_text_numbers)

print('These numbers could be telemarketers: ')
for number in possible_telemarketers:
    print(number)
