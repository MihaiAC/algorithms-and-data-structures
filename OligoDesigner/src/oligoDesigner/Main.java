package oligoDesigner;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {
    
    public static LinkedList<FSAndLocation> splitSequence(String seq, int repeatMinLen, int partMinLen, int partMaxLen, int maxPartCommonSeq) {
        seq = seq.toUpperCase();
        System.out.println(seq.length());
        int len = seq.length();
        int[] seqSFA = SuffixArray.buildSuffixArray(seq,len);
        int[] invSFA = new int[len]; 
        //inverse of SFA; SFA[i] = j => SFA[j] = i;
        for(int i=0; i<len; i++) {
            invSFA[seqSFA[i]] = i;
        }
        int[] LCP = Kasai.buildLCP(seq,seqSFA,len,invSFA);
        for(int i=0; i<len; i++) {
            System.out.println(i + " " + LCP[i] + " " + seq.substring(seqSFA[i],len) + " " + seqSFA[i]);
        }
        ArrayList<FmxrTuple> repeats = Findmaxr.findmaxr(seq,len,seqSFA,LCP,repeatMinLen,invSFA);
        
        HashMap<String,ArrayList<Integer>> fsPositions;
        HashMap<String,HashSet<String>> constraintGraph;
        fsPositions = FusionSite.generateFusionSites(seq);
        ArrayList<String> aL1 = new ArrayList<>(fsPositions.keySet());
        constraintGraph = FusionSite.generateConstraintGraph(aL1);
        
        //Must initialise a FusionSite object first.
        FusionSite fs = new FusionSite(seq,seqSFA,repeats,partMinLen,partMaxLen,repeatMinLen,maxPartCommonSeq,fsPositions,constraintGraph);
        LinkedList<FSAndLocation> ans = fs.findFusionSites();
        System.out.println(constraintGraph);
        return ans;
    }
    
    public static void main(String[] args) {
        String seq = args[0];
        System.out.println(splitSequence(seq,15,45,200,10).toString());
    }
    
    
    
}
