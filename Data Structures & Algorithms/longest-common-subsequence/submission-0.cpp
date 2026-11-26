class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        // create 2d grid based off texts (i.e. text1 are the units to the side (row) and text2  are the units above (columns)) where all the elements are initialised to 0. if text1[r] = text2[c], make grid element 1 and move diagonally
        int row = size(text1);
        int col = size(text2);
        vector<vector<int>> dp(row + 1, vector<int>(col + 1, 0));
        for (int r = row -1; r >=0; r--) {
            for (int c = col - 1; c >= 0; c--) {
                if (text1[r] == text2[c]) {
                    dp[r][c] = 1 + dp[r + 1][c + 1];
                }
                else {
                    dp[r][c] = max(dp[r+ 1][c], dp[r][c+1]);
                }
            }
        }
        return dp[0][0];
    }
};
