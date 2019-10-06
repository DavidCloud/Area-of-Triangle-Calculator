# Intro-to-computer-science
The Bubble-Sort algorithm is a very common sorting algorithm in programming. 
Its main purpose is to quickly sort through an array and place the elements of the array in ascending order. 
It does this by comparing adjacent elements and swapping if the second element is less than the first. 
Using the Bubble-Sort algorithm, it will continue to do this process through the entire length of the array until has been processed. 
The time complexity for the Bubble-Sort algorithm is dependent on the array, however the best case for it is O(n) where the worst case is O(n*n). 
The worst case for the Bubble-Sort algorithm would entail that the entire array had to be sorted if it was completely out of order. 
// Java program for implementation of Bubble Sort 
class BubbleSort 
{ 
    void bubbleSort(int arr[]) 
    { 
        int n = arr.length; 
        for (int i = 0; i < n-1; i++) 
            for (int j = 0; j < n-i-1; j++) 
                if (arr[j] > arr[j+1]) 
                { 
                    // swap arr[j+1] and arr[i] 
                    int temp = arr[j]; 
                    arr[j] = arr[j+1]; 
                    arr[j+1] = temp; 
                } 
    } 
  
    /* Prints the array */
    void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BubbleSort ob = new BubbleSort(); 
        int arr[] = {64, 34, 25, 12, 22, 11, 90}; 
        ob.bubbleSort(arr); 
        System.out.println("Sorted array"); 
        ob.printArray(arr); 
    } 
} 

List and Iterator ADTs
public class HelloWorld{

     class bubbleSort
     {
         void sortBubble(int oldAR[])
         {
             //Sorted Array
             int newARy[];
             
             //Sorting the Array
             int n = arr.length();
             for (int i = 0; i < n-1; i++)
             {
                 if(oldAR[i] < oldAR[i+1])
                 {
                     newAR[i] == oldAR[i];
                 }
                 else
                 {
                    newAR[i] == oldAR[i+1];
                 }
             }
             system.out.println("Sorted Array:/n" + newAR)
         }
     }
}
