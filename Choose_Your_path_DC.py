#Name: David Cloud
#Period: 7th
#Date: october 13th, 2016
#Assignment: Choose your path
#Scope: This program will allow the user to pick their path through a story

print ("You wake up in the middle of a jungle what do you do: Go back to sleep or Explore your surrondings");
A1 = input();

if A1 == "Go back to sleep":
    print ("You went back to bed for a while and a few hours later was awaken by a giant tiger. Do you Fight the Tiger or Run Away");
    A1a = input();
elif A1 == "Explore your surrondings":
    print ("You atart to explore around the jungle and eventually come up on what seems to be wreckage from a plane. Do you Explore the Plane or Keep Exploring the Jungle");
    A1b = input();
elif A1 != "Go back to sleep" or "Explore your surrondings":
    print("That was not a choice you can either 'Go back to sleep' or 'Explore your surrondings'");
    
if A1a == "Fight the tiger":
    print ("You fight the tiger and after jumping into the river you escape it. Do you swim upstream or downstream");
    A2a = input()
elif A1a == "Run Away":
    print ("You start to run away from the tiger, but it chases after you. Do you want to climb up a tree, or jump into the river");
    A2aa = input();
elif A1a != "Fight the Tiger" and "Run Away":
    print ("That is not an option. You can either 'Fight the Tigher' or 'Run Away'")

if A1b == "Explore the Plane":
    print ("You go into the plane and find your stuff on it and come to the conclusion that you were in a plane wreck and do not remember what happened. Do you want to Look for Materials on the Plane or Leave the Plane");
    A2b = input();
elif A1b == "Keep Exploring the Jungle":
    print("You go past the plane wreck and keep exploring and come up to a small tent. Do you want to See if anyone is there or Run away from the tent");
    A2bb = input();
    
