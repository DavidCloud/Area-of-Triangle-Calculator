#Name: David Cloud
#Period: 7th
#Date: September 12th, 2016
#Assignment: 2.6 Find Numbers of Years
#Scope: This program will convert a given value to the  number of years

print ("Enter a value of minutes you would like converted to years"); #This ask for the time and minutes
minutes = int(input());

hours = (minutes/60); #converts minutes to hours
days = (hours/24); #converts hours to days
years = (days/365); #converts days to years

L = years - int(years); #pulls the decimal from years to use to find days

#Converts the remainder amount of time to days
D = int(L * 365)


print (str(int(years)) + " years and " + str(D) + " days");#Prints the final answer