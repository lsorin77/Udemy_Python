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

telemarketers = []
non_telemarketers = []

for item in calls:
    if item[0] not in telemarketers:
        telemarketers.append(item[0])
    non_telemarketers.append(item[1])

for item in texts:
    non_telemarketers.append(item[0])
    non_telemarketers.append(item[1])

for item in telemarketers:
    if item in non_telemarketers:
        telemarketers.remove(item)

telemarketers.sort()

print("These numbers could be telemarketers: ")

prev_item = ''
for item in telemarketers:
    if item != prev_item:
        print(item)
        prev_item = item

