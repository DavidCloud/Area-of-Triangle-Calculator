#Name: David Cloud
#Period: 7th
#Date: November 11th, 2016
#Assignment: Math Help
#Scope: This program will let the user choose what math level they are at and give them math problems for practive based on the difficulty they chose

import random

Level = 0;
number = 0;

print ("What level of math are you: 1, 2, 3, or 4");
Level = int(input());

while Level == 1 or Level == 2 or Level == 3 or Level == 4:
    if Level == 1:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        print ("What is", str(random.choice(number)), "+", str(random.choice(number)));
        
    elif Level == 2:
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
    elif Level == 3:
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
    elif Level == 4:
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];