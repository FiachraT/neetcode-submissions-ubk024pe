class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def pal_check(l, r, count):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r+=1
                count +=1
            return count

        
        for i in range(len(s)):
            count = pal_check(i, i, count)
            count = pal_check(i, i + 1, count)
        return count
        