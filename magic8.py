# Author: Vernell Mangum
#
# Description: Simple python program that is essentially a Magic 8 Ball

import random

# Initial variable set up

name = "Vernell"

question = "Am I the best looking man of all time?"

answer = ""

# Initializing random number generator

random_number = random.randint(1, 12)

# Testing for random numbers
# print(random_number)

# Core logic for Magic 8Ball answers using an if / elif / else
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
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Are you serious?"
elif random_number == 11:
    answer = "I believe you're asking the wrong 8 Ball"
elif random_number == 12:
    answer = "Let me check with the 9 Ball"
else:
    answer = "Error"
    

    
# Error handling: No name or question was given
if question == "":
    print("There is no question for the 8 Ball to answer :/")
elif (name == "") and (question != ""):
    print("Question: " + question) # Asking the question
else:
    # Printing the question and Magic 8Ball answer
    print(name + " asks: " + question) # Asking the question
    
print("Magic 8Ball's answer: " + answer) # 8Ball answer