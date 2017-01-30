/*David Cloud
 * Period 7
 * January 19, 2017
 * The purpose of this program is to convert a fahrenheit temperature to celsius
 */

import java.util.Scanner;//Imports the scanner utility to allow for user input

public class TemperatureConversion {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);//Establishes scanner within public class
		
		System.out.print("Please enter a value in fahrenheit:");//Prompts user
		double fahrenheit = input.nextDouble();//Allows Input
		
		double celsius = (5.0 / 9) * (fahrenheit - 32);//Converts the inputed fahrenheit degree to celsius
		
		System.out.println(fahrenheit + " degrees in fahrenheit is " + celsius + " degrees in celsius"); //Prints back to the user
		
	}

}
