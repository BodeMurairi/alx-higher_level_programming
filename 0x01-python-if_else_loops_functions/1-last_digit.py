#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0 :
    new_number = number * -1
    last_digit = new_number % 10
else:
    new_number = number
    last_digit = number % 10
if last_digit > 5:
    print("Last digit of {} is {}, and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {}".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {}, and is less than 6 not 0".format(number, last_digit))
