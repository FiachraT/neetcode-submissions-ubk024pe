import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       nums = heapq.nlargest(k, nums)
       return nums[k - 1]
        