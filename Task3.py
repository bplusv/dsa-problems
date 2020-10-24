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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


unique_codes = set()
from_bangalore = 0
from_and_to_bangalore = 0

for call in calls:
    calling_number, answering_number = call[0], call[1]
    if calling_number[0:5] == '(080)':
        from_bangalore += 1
        if answering_number[0:2] == '(0':
            r = answering_number.find(')')
            code = answering_number[1:r]
            unique_codes.add(code)
            if code == '080':
                from_and_to_bangalore += 1
        elif answering_number[0] in ('7', '8', '9'):
            unique_codes.add(answering_number[0:4])
        elif answering_number[0:4] == '140':
            unique_codes.add('140')

unique_sorted_codes = list(unique_codes)
unique_sorted_codes.sort()
print('The numbers called by people in Bangalore have codes:')
for code in unique_sorted_codes:
    print(code)

percentage = from_and_to_bangalore / from_bangalore
print(f'{percentage:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
