#David Cloud
#Period Number:
#September 12th, 2016
#Geometry, Area of a Triangle
#Scope: (What is the purpose of the program?)

import math

print ("Enter your first set of points, X first then Y"); #Point A
X1 = float(input());
Y1 = float(input());

print ("Enter your second set of points, X first then Y"); #Point B
X2 = float(input());
Y2 = float(input());

print ("Enter your third set of points, X first then Y"); #Point C
X3 = float(input());
Y3 = float(input());


S1 = (math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)); #Side 1 (AB)
S2 = (math.sqrt((X3 - X2)**2 + (Y3 - Y2)**2)); #Side 2 (BC)
S3 = (math.sqrt((X3 - X1)**2 + (Y3 - Y1)**2)); #Side 3 (AC)

S = (S1 + S2 + S3)/2;

A = math.sqrt(S(S-S1)(S-S2)(S-S3));

print (A);




