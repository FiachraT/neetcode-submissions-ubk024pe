class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return list of all unique combinations, therefore backtracing
        #if target reached, add to result
        # 2 choices, add current number or move on, compare to target afterwards
        res = []
        subset = []
        total = 0

        def dfs(i, total):

            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            subset.append(nums[i])
            total += nums[i]
            dfs(i, total)
            total -= subset.pop()
            dfs(i + 1, total)
        
        dfs(0, total)
        return res



        