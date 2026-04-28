"""
Experiment: 04
Program: Even or Odd Number
Author: Abhishek Choudhery
Description: Python program to check whether a number is even or odd using conditional statements.
"""

# Taking input from the user
num = int(input("Enter a number: "))

# Checking even or odd
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")