class Solution {
    public int arrangeCoins(int n) {
        int level = 0;
        while (n >= 0) {
            n -= (level + 1);
            if (n >= 0) {
                level += 1;
            }
        }
        return level;
    }
}