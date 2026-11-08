class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #keep track of current max, current min, temp max, max_output
        cur_max = cur_min = max_res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_max *= num
            cur_min *= num
            temp = cur_max  # temp saved cur_max

            cur_max = max(num, cur_max, cur_min) #cur_max overwriten
            cur_min = min(num, temp, cur_min)  # temp saved cur_max

            max_res = max(cur_max, max_res)
        return max_res
        