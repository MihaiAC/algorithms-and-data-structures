package oligoDesigner;

public class FSAndLocation {
    String FS;
    Integer location;
    
    public FSAndLocation(String fs, int location) {
        this.FS = fs;
        this.location = location;
    }
    
    @Override
    public String toString() {
        return "("+FS+","+location.toString()+")";
    }
}
