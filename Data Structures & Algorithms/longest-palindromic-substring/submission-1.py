class Solution:
    def longestPalindrome(self, s: str) -> str:
        # l and r pointer surely
        # 2 choices, at any point move the l or r pointer
        # max 2 sub problems, even lenght palindrome and odd length palindrome
        def pal_check(l, r):
            if s[l] != s[r] and s[l] != s[r - 1]:
                return 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (r - l - 2, l + 1, r - 1)
            
        max_pal = (0, 0, 0)
        for i in range(len(s) - 1):
            # max(odd, even)
            bigger = max(pal_check(i, i), pal_check(i, i + 1))
            max_pal = max(max_pal, bigger)
            print(max_pal)
        t, l, r = max_pal
        return s[l:r+ 1]
        




        