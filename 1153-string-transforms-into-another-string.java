import java.util.HashMap;
import java.util.HashSet;

class Solution1153 {
    public boolean canConvert(String str1, String str2) {
        if (str1.equals(str2)) {
            return true;
        } 
        
        int n = str1.length();
        
        HashSet<Character> strs2 = new HashSet<Character>();
        
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        for (int i = 0; i < n; i++) {
            if (!strs2.contains(str2.charAt(i))) {
                    strs2.add(str2.charAt(i));
            }
            if (!map.containsKey(str1.charAt(i))) {
                map.put(str1.charAt(i), str2.charAt(i));
            } else {
                if (map.get(str1.charAt(i)) != str2.charAt(i)) {
                    return false;
                }
            }
        }
        
        return strs2.size() < 26;
    }
}