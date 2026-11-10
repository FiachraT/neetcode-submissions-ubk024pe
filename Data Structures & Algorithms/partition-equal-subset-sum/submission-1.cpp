#include <numeric>
class Solution {
public:
    bool canPartition(vector<int>& nums) {
      // if found return True,  if none found return False
      int total = accumulate(nums.begin(), nums.end(), 0);
      if (total % 2 == 1) {
        return false;
      }
      int target = total / 2;
      int n = nums.size();
      int num;
      vector<bool> dp(target + 1, false); // d[x] = true if a subset of the numbers considered so far can sum to x
      dp[0] = true;
      for (int i = 0; i < n; i++) {
        num = nums[i];
        for (int x = target; x >= num; x--) {
            dp[x] = dp[x] || dp[x - num];
        }
      }
      return dp[target];
    }
};
