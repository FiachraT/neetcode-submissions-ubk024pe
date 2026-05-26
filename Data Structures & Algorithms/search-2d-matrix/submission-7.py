class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top, bot = 0, m - 1
        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        if top > bot:
            return False
        l = 0
        r = n - 1
        while l <= r:
            c = l + (r - l) // 2
            val = matrix[mid][c]
            print(l, c, r, mid, val, target)
            if target == val:
                return True
            elif target < val:
                r = c - 1
            else:
                l = c + 1
        return False
                
                


