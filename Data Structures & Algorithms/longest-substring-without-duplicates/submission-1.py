class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # O(N)
        # hash map
        seen = {}
        l = 0
        max_len = 0
        for r, c in enumerate(s):
            if c in seen:
                l = max(seen[c] + 1, l)
            seen[c] = r
            max_len = max(r-l + 1, max_len)
        return max_len