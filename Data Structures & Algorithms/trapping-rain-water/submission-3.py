class Solution:
    def trap(self, height: List[int]) -> int:
        # water at any given point can be calculated as 
        # min(max_left, max_right) - height[i]
        # O(N)

        l = 0 
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        water = 0
        while l < r:
            if max_left < max_right:
                l+=1
                h = height[l]
                if h < max_left:
                    water += max_left - h
                else:
                    max_left = h 
            else:
                r-=1      
                h = height[r]
                if h < max_right:
                    water += max_right - h
                else:
                    max_right = h 
        return water     
        