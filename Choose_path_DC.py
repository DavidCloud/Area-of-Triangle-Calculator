#Name: David Cloud
#Period: 7th
#Date: october 20th, 2016
#Assignment: Choose your path
#Scope: This program will allow the user to pick their path through a story

print ("You wake up in the middle of a jungle what do you do: Go back to Sleep (1) or Explore your surrondings (2)"); #Question 1
Question1 = int(input()); #Input for Question 1

if Question1 == 1: #Option 1 for Question 1
    print ("You went back to bed for a while and a few hours later was awaken by a giant tiger. Do you Fight the Tiger (1) or Run Away (2)"); #Question 2
    Question2a = int(input()); #Answer for question 2
    if Question2a == 1: #Option 1 for Question 2
        print ("You fight the tiger and after jumping into the river you escape it. Do you swim upstream (1) or downstream (2)"); #Question 3 for first option of Question 1
        Question3a = int(input()); #Input for Question 3 of option 1 for Question 2
    elif Question2a == 2: #Option 2 for Question 2
        print ("You start to run away from the tiger, but it chases after you. Do you want to climb up a tree (1), or jump into the river (2)"); #Question 3 for second option of Question 1
        Question3b = int(input()); #Option 2 for question 3 of option 2 for Question 2
    if Question3a == 1: #Option 1 for Question 3
        print ("You climb the tree and get about 20 feet up it when the tiger runs off. Do you want to go back down and try to gather materials (1) or stay in the tree for a few hours (2)"); #Question 4 for first option of Question 3
        Question4a = int(input()); #Input for Question 4 for option 1 of Question 3
    elif Question3b == 2: #Option 2 for Question 3
        print ("You jump into a river and see several big fish swimming towards you. Do you want to swim upstream away from the fish (1) or downstream towards the firsh (2)"); #Question 4 for second option of Question 3
        Question4b = int(input()); #Input for Question for option 2 of Question 3
            
            
if Question1 == 2: #Option 2 for Question 1
    