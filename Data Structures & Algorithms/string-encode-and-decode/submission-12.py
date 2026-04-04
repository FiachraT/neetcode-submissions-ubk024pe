class Solution:

    def encode(self, strs: List[str]) -> str:
        ns = ""
        for s in strs:
            ns += str(len(s)) + "#" + s
        return ns

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            r = l
            while r < len(s) and s[r] != "#":
                r+=1
            new_s = r + int(s[l:r]) + 1
            res.append(s[r+ 1: new_s])
            l  =  new_s
        return res
            
        
