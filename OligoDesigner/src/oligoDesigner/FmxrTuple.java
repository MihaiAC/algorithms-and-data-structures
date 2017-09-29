package oligoDesigner;

public class FmxrTuple {
    
    public Integer posInSFA;
    public Integer nrOfOccurences;
    public Integer length;
    
    public FmxrTuple(int p, int n, int l) {
        this.posInSFA = p;
        this.nrOfOccurences = n;
        this.length = l;
    }
    
    @Override
    public String toString() {
        return "("+posInSFA.toString()+","+nrOfOccurences.toString()+","+length.toString()+")";
    }
}
