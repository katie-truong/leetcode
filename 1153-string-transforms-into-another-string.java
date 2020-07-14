/*
- Create a mapping between the characters of str1 and str2. 
- For each character of str1, it can only map to another character in str2. If a character has two mappings, the conversion is impossible.
- If str2 contains 26 unique characters, there would be no "temp" character to transfer for the conversion. Hence, it's impossible, 
unless str1 is exactly equal to str2.
- Optimization: We can count the number of unique characters in str2 inside the same for loop (and only having 1 iteration).
*/

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