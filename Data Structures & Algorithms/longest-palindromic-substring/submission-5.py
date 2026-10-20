class Solution:
    def longestPalindrome(self, s: str) -> str:
        # l and r pointer surely
        # 2 choices, at any point move the l or r pointer
        # max 2 sub problems, even lenght palindrome and odd length palindrome
        def pal_check(l, r)-> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
           p1 = pal_check(i, i)
           p2 = pal_check(i, i + 1)

           if len(p1) > len(res):
            res = p1
           if len(p2) > len(res):
            res = p2
        return res

            
        




        