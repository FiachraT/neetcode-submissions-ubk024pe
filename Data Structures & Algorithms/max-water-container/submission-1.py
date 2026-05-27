class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find water at any given i, by keeping track of the current max height and subtracting that by the height of the water
        # two pointer
        # the one that is smaller moves

        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            max_height = min(heights[l], heights[r])
            max_area = max(max_area, max_height*(r-l))
            if max_height < heights[l]:
                r-=1
            else:
                l+=1
        return max_area

