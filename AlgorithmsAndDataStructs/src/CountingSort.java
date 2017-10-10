//Useful if range is not significant;y greater than the input size.

public class CountingSort {
    public static void countingSort(int[] arr, int range) {
        int count[] = new int[range+1];
        
        //Count the number of apparitions of each element in count[].
        for(int i=0; i<arr.length; i++) {
            count[arr[i]]++;
        }
        
        //Element at each index stores the sum of previous counts => indicates the position of each object in the output sequence.
        for(int i=1; i <= range; i++) {
            count[i] += count[i-1];
        }
        
        
        int[] output = new int[arr.length];
        //O(n+k) extra space, O(n) - time;
        //Effect: whenever a character in arr is found, put it in its position and decrease the count by 1.
        //It is correct because the elements with 0 count are not met!!.
        for (int i = 0; i<arr.length; i++) {
            output[count[arr[i]]-1] = arr[i]; // -1 because the count starts from 1, not 0.
            --count[arr[i]];                  // decrease the count of arr[i];
        }
        
        for(int i=0; i<arr.length; i++) {
            arr[i] = output[i];
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {3,6,20,34,10};
        countingSort(arr,34);
        System.out.println(java.util.Arrays.toString(arr));
    }
}
