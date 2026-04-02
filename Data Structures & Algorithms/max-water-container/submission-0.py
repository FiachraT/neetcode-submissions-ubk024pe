class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, if l < r, move l right
        # Record max height
        # only need to record maximum area
        # only record max limit, need to take into account distance between l and r

        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            limit = min(heights[l], heights[r])
            area = limit*(r-l)
            max_area = max(max_area, area)
            print(l, r, area)
            if heights[l] < heights[r]:
                l +=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return max_area

            