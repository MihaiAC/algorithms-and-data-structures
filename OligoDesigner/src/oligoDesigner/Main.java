package oligoDesigner;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {
    
    public static LinkedList<FSAndLocation> splitSequence(String seq, int repeatMinLen, int partMinLen, int partMaxLen, int maxPartCommonSeq) {
        //Make the sequence uppercase.
        seq = seq.toUpperCase();
        int len = seq.length();
        String extendedSeq = seq + FusionSite.reverseComplement(seq); //extendedSeq contains the sequence and its 
                                                                      //reverse complement back to back;
        
        int[] seqSFA = SuffixArray.buildSuffixArray(extendedSeq,2*len); //create suffix array of the extended sequence;
        int[] invSFA = new int[2*len];                                  //inverse of SFA;
        
        //Inverse of SFA; SFA[i] = j => SFA[j] = i;
        for(int i=0; i<2*len; i++) {
            invSFA[seqSFA[i]] = i;
        }
        
        //Calculate the largest common preffix (LCP) array.
        int[] LCP = Kasai.buildLCP(extendedSeq,seqSFA,2*len,invSFA);
        
        //Find the repeats larger than repeatMinLen.
        ArrayList<FmxrTuple> repeats = Findmaxr.findmaxr(extendedSeq,2*len,seqSFA,LCP,repeatMinLen,invSFA);
        
        HashMap<String,ArrayList<Integer>> fsPositions;             //fusion sites and their positions in the array;
        HashMap<String,HashSet<String>> constraintGraph;            //<s1:s2> is in constraintGraph if s1 and s2 cannot 
                                                                    //be selected as fusion sites at the same time;
        
        //We will use only the fusion sites in the normal sequence (we don't need the ones in the extended seq).
        fsPositions = FusionSite.generateFusionSites(seq);
        ArrayList<String> aL1 = new ArrayList<>(fsPositions.keySet());
        constraintGraph = FusionSite.generateConstraintGraph(aL1);
        
        
        //Initialising a FusionSite object.
        FusionSite fs = new FusionSite(seq,seqSFA,repeats,partMinLen,partMaxLen,repeatMinLen,maxPartCommonSeq,fsPositions,constraintGraph);
        LinkedList<FSAndLocation> ans = fs.findFusionSites();
        return ans;
    }
    
    public static void main(String[] args) {
        String seq = args[0];
        System.out.println(splitSequence(seq,15,45,200,10).toString());
        System.out.println(FusionSite.reverseComplement(seq.toUpperCase()));
    }
    
    
    
}
