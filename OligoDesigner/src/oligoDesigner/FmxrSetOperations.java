package oligoDesigner;

public final class FmxrSetOperations {
    /*
     * The set S is represented by an array of integers. 
     * Size of array: 2n+1, n = length of the sequence. 
     * The leaves are from n to 2n.
     * 
     * S[i] = 0 if i in [n,2n] and i-n is not in the set 
     *          OR i in [0,n] and S[2*i]=S[2*i+1]=0.
     *          
     * S[i] = 1 if i in [n,2n] and i-n is in the set
     *          OR i in [0,n] and S[2*i]=1 OR S[2*i+1]=1.
     */
    private FmxrSetOperations() {}
    
    public static int[] buildSet(int n) {
        int[] S = new int[2*n+1];
        for(int i=0; i<2*n+1; i++) {
            S[i] = 0; //probably redundant.
        }
        return S;
    }
    
    //elem must be in 0..n
    public static void addElem(int[] S, int elem, int n) {
        S[elem+n] = 1;
        int aux = elem+n;
        while(aux != 1) {
            aux = aux/2;
            S[aux] = 1;
        }
    }
    
    public static int log2(int elem) {
        int power = 0;
        if(elem == 1) {
            return 0;
        }
        else {
            while(elem > 0) {
                elem = elem/2;
                power++;
            }
        }
        return --power;
    }
    
    //elem must be in n..2n
    public static int maxLessThan(int[] S, int elem, int len) {
        int currIndex = elem+len;
        //topmost node will always be 1 => no need checking;
        while(S[currIndex] != 1) {
            //If current node is a left child:
            if((currIndex/2)*2 == currIndex) {
                if(log2(currIndex-1) != log2(currIndex)) {
                    System.err.println("Rightmost node to the left of the current node not found.");
                }
                currIndex--;
                continue;
            }
            else {
                currIndex = currIndex/2;
                if(currIndex == 0) {
                    System.err.println("There is no parent node.");
                }
                continue;
            }
        }
        while(currIndex < len) {
            if(S[2*currIndex+1] == 1) {
                currIndex = 2*currIndex+1;
            }
            else {
                currIndex = 2*currIndex;
            }
        }
        return currIndex;
    }
    
    public static int minGreaterThan(int[] S, int elem, int len) {
        int currIndex = elem+len;
        //topmost node will always be 1 => no need checking;
        while(S[currIndex] != 1) {
            //If current node is a right child:
            if((currIndex/2)*2+1 == currIndex) {
                if(log2(currIndex+1) != log2(currIndex)) {
                    System.err.println("Leftmost node to the right of the current node not found.");
                    System.out.println(currIndex);
                    System.out.println(len);
                    System.out.println(elem);
                }
                currIndex--;
                continue;
            }
            else {
                currIndex = currIndex/2;
                if(currIndex == 0) {
                    System.err.println("There is no parent node.");
                }
                continue;
            }
        }
        while(currIndex < len) {
            if(S[2*currIndex+1] == 1) {
                currIndex = 2*currIndex+1;
            }
            else {
                currIndex = 2*currIndex;
            }
        }
        return currIndex;
    }
    
    
    
    public static void main(String[] args) {
        System.out.println(log2(3));
    }
}
