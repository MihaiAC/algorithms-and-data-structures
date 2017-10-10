package oligoDesigner;

import java.util.ArrayList;

public class RepeatPair {
    public Integer fst;    //first Index
    public Integer snd;    //second Index
    public Integer length; //length of the repeat
    public Integer dir;    //direction of the repeat; 1 forward -1 backward;
    
    public RepeatPair(int fst, int snd, int length, int dir) {
        this.fst = fst;
        this.snd = snd;
        this.length = length;
        this.dir = dir;
    }
    
    //We don't care about nested repeats.
    public static ArrayList<RepeatPair> FmxrTupleListTORepeatPairList(int len, ArrayList<FmxrTuple> fmxr, int repeatMinLen, 
                                                                      int partMaxLen, int[] seqSFA) {
        ArrayList<RepeatPair> repeats = new ArrayList<>();
        for(int i=0; i<fmxr.size(); i++) {
            FmxrTuple aux = fmxr.get(i);
            
            int[] indices = new int[aux.nrOfOccurences];
            
            //Save the indices of the repeats in the original string.
            for(int j=0; j<aux.nrOfOccurences; j++) {
                indices[j] = seqSFA[aux.posInSFA+j];
            }
            
            //indices[i] < indices[j], for any i<j (due to how the SFA was constructed) -> WRONG ASSUMPTION.
            java.util.Arrays.sort(indices);
            
            
            //Analyze every pair of repeats.
            for(int j=0; j<aux.nrOfOccurences-1; j++) {
                for(int k=j+1; k<aux.nrOfOccurences; k++) {
                    //If both repeats are in the reverse complement, discard them (they are accounted for by their 
                    //forward complements).
                    if(indices[j] >= len && indices[k] >= len) {
                        continue;
                    }
                    
                    
                    if(indices[j]+aux.length-1 <= indices[k]) {
                        RepeatPair rp = new RepeatPair(indices[j],indices[k],aux.length);
                        repeats.add(rp);
                    }
                    else {
                        int commonLen = indices[j] + aux.length - indices[k]; //-1 + 1 - cancelled out
                        if(aux.length-commonLen >= repeatMinLen) {
                            RepeatPair rp1 = new RepeatPair(indices[j],indices[k],aux.length-commonLen);
                            repeats.add(rp1);
                            RepeatPair rp2 = new RepeatPair(indices[k]+2*commonLen-aux.length-1,indices[k]+commonLen,aux.length-commonLen);
                            repeats.add(rp2);
                        }
                    }
                }
            }
        }
        return repeats;
    }
    
    @Override
    public String toString() {
        return "("+fst.toString()+","+snd.toString()+","+length.toString()+")";
    }
}
