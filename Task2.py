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
numbers = {}
lon_time = {'number': '', 'duration': 0}


def check_number(number, duration):
    numbers[number] = numbers.get(number, 0) + duration

    if numbers[number] > lon_time['duration']:
        lon_time['number'] = number
        lon_time['duration'] = numbers[number]


for item in calls:
    check_number(item[0], int(item[3]))
    check_number(item[1], int(item[3]))

print(f"{lon_time['number']} spent the longest time, {lon_time['duration']} seconds, on the phone during September 2016.")

