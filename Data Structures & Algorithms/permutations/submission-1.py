class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                
                path.append(nums[i])
                visited[i] = True
                dfs(path)
                visited[i] = False
                path.pop()

        dfs([])
        return res
        