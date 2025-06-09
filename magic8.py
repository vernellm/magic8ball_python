# Author: Vernell Mangum
#
# Description: Simple python program that is essentially a Magic 8 Ball

import random

# Initial variable set up

name = "Vernell"

question = "Am I the best looking man of all time?"

answer = ""

# Initializing random number generator

random_number = random.randint(1, 9)

# Testing for random numbers
# print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so goo"
elif random_number == 9:
    answer = "YVery doubtful"
else:
    answer = "Error"