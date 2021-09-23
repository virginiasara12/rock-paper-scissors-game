# game.py

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print("-------------------")
print("Welcome", x, "to my Rock-Paper-Scissors game...")


import random

print("-------------------")
print("Rock, Paper, Scissors, Shoot!")

# prompt user for input

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")

if user_choice not in ["rock", "paper", "scissors"]:
    print("Sorry, invalid input. Please try again.")
    exit()

print("You chose:", user_choice)

# computer choice (at random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:", computer_choice)

print("-------------------")

if user_choice == computer_choice:
    print("It's a tie!")

if user_choice == "rock" and computer_choice == "scissors":
    print("Congrats! You won!")
if user_choice == "rock" and computer_choice == "paper":
    print("Oh, the computer won. It's ok.")


if user_choice == "paper" and computer_choice == "scissors":
    print("Oh, the computer won. It's ok.")
if user_choice == "paper" and computer_choice == "rock":
    print("Congrats! You won!")


if user_choice == "scissors" and computer_choice == "rock":
    print("Oh, the computer won. It's ok.")
if user_choice == "scissors" and computer_choice == "paper":
    print("Congrats! You won!")

print("-------------------")
print("Thanks for playing. Please play again!")