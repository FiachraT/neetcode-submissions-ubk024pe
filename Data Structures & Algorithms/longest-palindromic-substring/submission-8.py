class Solution:
    def longestPalindrome(self, s: str) -> str:
         # fr loop checking each character
         n = len(s)

         def pal_check(l, r):
            while r < n and l >=0 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
         max_pal = ""
         for i in range(len(s)):
            res1 = pal_check(i, i)
            res2 = pal_check(i, i + 1)
            if len(res1) > len(max_pal):
                max_pal = res1
            if len(res2) > len(max_pal):
                max_pal = res2
         return max_pal

            
        