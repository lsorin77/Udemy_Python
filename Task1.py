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
numbers = []


def check_number(number):
    if number not in numbers:
        numbers.append(number)


def get_numbers(number_list):
    for item in number_list:
        check_number(item[0])
        check_number(item[1])


get_numbers(texts)
get_numbers(calls)

print(f"There are {len(numbers)} different telephone numbers in the records.")
