package oligoDesigner;

import java.util.ArrayList;

public class RepeatPair {
    public Integer fst;    //first Index
    public Integer snd;    //second Index
    public Integer length; //length of the repeat
    
    public RepeatPair(int fst, int snd, int length) {
        this.fst = fst;
        this.snd = snd;
        this.length = length;
    }
    
    //We don't care about nested repeats.
    public static ArrayList<RepeatPair> FmxrTupleListTORepeatPairList(ArrayList<FmxrTuple> fmxr, int repeatMinLen, 
                                                                      int partMaxLen, int[] seqSFA) {
        ArrayList<RepeatPair> repeats = new ArrayList<>();
        for(int i=0; i<fmxr.size(); i++) {
            FmxrTuple aux = fmxr.get(i);
            int[] indices = new int[aux.nrOfOccurences];
            
            //Save the indices of the repeats in the original string.
            for(int j=0; j<aux.nrOfOccurences; j++) {
                indices[j] = seqSFA[aux.posInSFA+j];
            }
            
            java.util.Arrays.sort(indices);
            //Sort FmxrTuple based on length first.
            
            
            //Analyze every pair of repeats.
            //indices[i] < indices[j], for any i<j (due to how the SFA was constructed) -> WRONG ASSUMPTION.
            for(int j=0; j<aux.nrOfOccurences-1; j++) {
                for(int k=j+1; k<aux.nrOfOccurences; k++) {
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
