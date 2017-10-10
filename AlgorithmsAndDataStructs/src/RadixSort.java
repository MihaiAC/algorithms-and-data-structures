
public class RadixSort {
    private static int countDigits(int i) {
        int count = 1;
        i = i/10;
        while(i != 0) {
            i = i/10;
            count++;
        }
        return count;
    }
    
    private static int maxNrOfDigits(int[] arr) {
        int maxDigits = 1, currDigits = 0;
        for(int i=0; i<arr.length; i++) {
            currDigits = countDigits(arr[i]);
            if(currDigits > maxDigits) {
                maxDigits = currDigits;
            }
        }
        return maxDigits;
    }
    
    private static void countingSort(int[] arr, int exp) {
        int len = arr.length, count[] = new int[10], output[] = new int[len];
        
        for(int i=0; i<len; i++) {
            count[(arr[i]/exp)%10]++;
        }
        
        for(int i=1; i<10; i++) {
            count[i] += count[i-1];
        }
        
        // From n-1 to 0 in order to preserve the order!!!.
        for(int i=len-1; i>=0; i--) {
            output[count[(arr[i]/exp)%10]-1] = arr[i];
            count[(arr[i]/exp)%10]--;
        }
        
        for(int i=0; i<len; i++) {
            arr[i] = output[i];
        }
    }
    
    public static void radixSort(int[] arr) {
        int maxNrDigits = maxNrOfDigits(arr);
        for(int exp=1; maxNrDigits > 0; exp *=10) {
            countingSort(arr,exp);
            maxNrDigits--;
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {2,256,34,34,23,0};
        radixSort(arr);
        System.out.println(java.util.Arrays.toString(arr));
    }
}
