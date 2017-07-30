public class Trie{
    
    public class TrieNode{
        public int count = 0;                 //Number of words which terminated here.
        public TrieNode[] arr;                //Holds continuation of other words.
        public TrieNode(){
            this.arr = new TrieNode[26];        
        }
        
    }
    
    private TrieNode root;
    
    public Trie() {
        this.root = new TrieNode();
    }
    
    public void insertWord(String word) {
        TrieNode currentPos = this.root;
        for(int wi=0; wi<word.length(); wi++) {
            int index = word.charAt(wi) - 'a';
            if(currentPos.arr[index] == null) {
                currentPos.arr[index] = new TrieNode();
                currentPos = currentPos.arr[index];
            }
            else {
                currentPos = currentPos.arr[index];
            }
        }
        currentPos.count++;
    }
    
    public boolean searchWord(String word) {
        if(word == null) {
            return false;
        }
        if(word.length() == 0) {
            return false;
        }
        
        TrieNode aux = searchNode(word);
        
        if(aux == null) {
            return false;
        }
        else {
            if(aux.count > 0) {
                return true;
            }
        }
        
        return false;
    }
    
    public boolean searchPrefix(String word) {
        TrieNode aux = searchNode(word);
        return (aux == null) ? false : true;
    }
    
    public TrieNode searchNode(String word) {
        TrieNode currentPos = this.root;
        for(int wi=0; wi < word.length(); wi++) {
            int index = word.charAt(wi) - 'a';
            if(currentPos.arr[index] == null) {
                return null;
            }
            else {
                currentPos = currentPos.arr[index];
            }
        }
        return currentPos;
    }
    
    public static void main(String[] args) {
        Trie t = new Trie();
        for(int i = 0; i < args.length; i++) {
            t.insertWord(args[i]);
        }
        System.out.println(t.searchPrefix("p"));
    }
}