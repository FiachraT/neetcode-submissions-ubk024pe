class Solution:
    def trap(self, height: List[int]) -> int:
        # key insight: height at any index is min(max_left, max_right) - height[i]
        l = 0
        r = len(height) - 1
        water = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if left_max <= right_max:
                l+= 1
                left_max = max(height[l], left_max)
                water += left_max - height[l]
            else:
                r-=1
                right_max = max(height[r], right_max)
                water += right_max - height[r]
        return water