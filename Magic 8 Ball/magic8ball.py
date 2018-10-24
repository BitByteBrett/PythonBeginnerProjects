#!/usr/bin/env python3
"""Recreate magic 8 ball

Usage:

    python3 magic8ball.py
"""

import random
import time
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


ask = "y"

answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtfu"]


while ask == "Y" or ask == "y" or ask == "Yes" or ask == "yes":
    clear()
    question = input("\n" + "What is your question? : ")
    print("\n" + "thinking...." + "\n")
    time.sleep(4)
    answer = random.choice(answers)
    print(answer)
    ask = input("\n" + "Would you like to ask another question? (Y or N): ")
