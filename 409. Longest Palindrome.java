class Solution {
    public int longestPalindrome(String s) {
        boolean letterArray[] = new boolean[58];
        int ans = 0;
        for(char c : s.toCharArray()){
            if(letterArray[(int)c-65]){
                ans += 2;
                letterArray[(int)c-65] = false;
            }else{
                letterArray[(int)c-65] = true;
            }
        }
        for(boolean a : letterArray){
            if(a){
                return ans + 1;
            }
        }
        return ans;
    }
}
