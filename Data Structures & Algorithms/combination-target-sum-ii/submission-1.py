class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset =[]

        def dfs(start, target):
            if target == 0:
                res.append(subset.copy())
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > target:
                    break
                if i > start and c == candidates[i - 1]:
                    continue
                subset.append(c)
                dfs(i+1, target - c)
                subset.pop()

        dfs(0, target)
        return res
        

        