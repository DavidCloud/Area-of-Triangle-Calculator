#Name: David Cloud
#Period: 7th
#Date: November 11th, 2016
#Assignment: Math Help
#Scope: This program will let the user choose what math level they are at and give them math problems for practive based on the difficulty they chose

import random;

#Variables set to be identified in while statements
Level = 0;
correct = 0;
incorrect = 0;
number1 = 0;
number2 = 0;
response = '';
MathType = '';

print ("What level of math are you: 1, 2, or 3");
Level = int(input());
print ("What type of math do you need help with. +, -, /, or *")
MathType = input();

#Math level 1 addition
if Level == 1 and MathType == '+':
    while response != 'N':
        number1 = random.randrange(0,11);
        number2 = random.randrange(0,11);  
        print ("What is", number1, "+", number2, "?");
        Uanswer = int(input());
        if Uanswer == number1 + number2:
            print ("You were correct!");
            correct += 1;
        else: 
            print ("You were incorrect!");
            incorrect += 1;
        print ("Would you like to continue? Y/N");
        response = input();
        if response == 'N':
            print ("You got", correct, "correct answers.");
            print ("You got", incorrect, "incorrect answers.");

#Math level 2 addition
if Level == 2 and MathType == '+':
    while response != 'N':
        number1 = random.randrange(0,51);
        number2 = random.randrange(0,51);
        print ("What is", number1, "+", number2, "?");
        Uanswer = int(input());
        if Uanswer == number1 + number2:
            print ("You were correct!");
            correct += 1;
        else: 
            print ("You were incorrect!");
            incorrect += 1;
        print ("Would you like to continue? Y/N");
        response = input();
        if response == 'N':
            print ("You got", correct, "correct answers.");
            print ("You got", incorrect, "incorrect answers.");
        
#Math level 3 addition
if Level == 3 and MathType == '+':
    while response != 'N':
        number1 = random.randrange(0,101);
        number2 = random.randrange(0,101);
        print ("What is", number1, "+", number2, "?");
        Uanswer = int(input());
        if Uanswer == number1 + number2:
            print ("You were correct!");
            correct += 1;
        else: 
            print ("You were incorrect!");
            incorrect += 1;
        print ("Would you like to continue? Y/N");
        response = input();
        if response == 'N':
            print ("You got", correct, "correct answers.");
            print ("You got", incorrect, "incorrect answers.");


if Level == 1 and MathType == '-':
    while response != 'N':
        number1 = random.randrange(0,11);
        number2 = random.randrange(0,11);
        number1 > number2; 
        print ("What is", number1, "-", number2, "?");
        Uanswer = int(input());
        if Uanswer == number1 - number2:
            print ("You were correct!");
            correct += 1;
        else: 
            print ("You were incorrect!");
            incorrect += 1;
        print ("Would you like to continue? Y/N");
        response = input();
        if response == 'N':
            print ("You got", correct, "correct answers.");
            print ("You got", incorrect, "incorrect answers.");
    
    
        
