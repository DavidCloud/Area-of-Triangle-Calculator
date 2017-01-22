#Name: David Cloud
#Period Number: 7th 
#September 15th, 2016
#Geometry: 2.7 Sum the digits in an integer
#Scope: 

print ("Enter a number between 0 and 1000");
I = int(input());

#N1 represents the last number in the digit
N1 = int(I % 10) 

#N2 represents the middle digit in the integer
N2 = int(I / 10)
N2a = int(N2 % 10)

#N3 represents the first digit in the integer
N3 = int(N2 / 10)
N3a = int(N3 % 10)


print (str(N1 + N2a + N3a)) #This prints the summ of the digits in the integer
