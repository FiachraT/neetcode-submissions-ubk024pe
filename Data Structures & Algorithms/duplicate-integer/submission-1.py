class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for c in nums:
            map[c] = map.get(c, 0) + 1
        if map and max(map.values()) > 1:
            return True
        return False
        