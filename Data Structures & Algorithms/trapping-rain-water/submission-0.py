class Solution:
    def trap(self, height: List[int]) -> int:
        # non negative integer
        # Need to find area between 2 bars and subtract area taken by bars inbetween. Flawed
        # new approach, lets go level by level, if we find there's one empty space, we count all the places on that level
        # which are free and add it to area, then we move the smaller side over one and see if we can check the next level
        # l and r must be equal to or surpase the level height to add the level
        # O(h *N), where h is the min height of the two smallest towers

        l = 0
        r = len(height) - 1
        area = 0
        prev_height = 0
        while l < r:
            left = height[l]
            right = height[r]
            h = min(left, right)
            if h > prev_height:
                for i in range(prev_height, h):
                    for j in range(l+1,r):
                        if height[j] <= i:
                            area += 1
                prev_height = h
            if left == right:
                l+=1
                r-=1
            elif left > right:
                r-=1
            else:
                l+=1
        return area
        

