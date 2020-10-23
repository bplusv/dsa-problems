"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

total_time = {}

for call in calls:
    incoming_number, answering_number, duration = call[0], call[1], int(call[3])
    total_time[incoming_number] = total_time.get(incoming_number, 0) + duration
    total_time[answering_number] = total_time.get(answering_number, 0) + duration

max_number = calls[0][0]
for number in total_time:
    if total_time[number] > total_time[max_number]:
        max_number = number

print(f'{max_number} spent the longest time, {total_time[max_number]} seconds, on the phone during September 2016.')
