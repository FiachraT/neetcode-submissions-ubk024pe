class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # 1 for loop then 2 sum
       nums.sort()
       res = []
       for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i -1]:  #no pint checking after left most pointer greater than 0
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
             threesum = a + nums[l] + nums[r]
             if threesum == 0:
                res.append([a, nums[l], nums[r]])
                l+=1
                r-=1
                while l < r and nums[l] == nums[l - 1]:
                    l+=1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
             elif threesum < 0:
                l+=1
             else:
                r-=1
       return res
        
