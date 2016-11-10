#Name: David Cloud
#Period: 7th
#Date: November 11th, 2016
#Assignment: Grades
#Scope: This program will let the user input grades and it will determine the highest grade, the lowest grade, and the average of all the grades

Positive = 0;
Negative = 0;
Total = 0;
Integers = 1;

print ("Enter an integer, the input ends if it is 0:")
Integers = int(input());

while Integers >= 0:
    
    if Integers > 0:
        Integers = Integers
        Positive = Positive + 1;
    elif Integers < 0:
        Negative = Negative + 1;
    else:
        print ("There are " + Positive + " positive integers");
        print ("There are " + Negative + " positive integers");
        print ("There are " + str(Positive + Negative) + " total integers");
        print ("The average of the integers is")        
        
        
