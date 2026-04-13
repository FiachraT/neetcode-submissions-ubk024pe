class Solution:

    def encode(self, strs: List[str]) -> str:
        ns = ""
        for s in strs:
            ns += str(len(s)) + "#" + s
        return ns

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = 0
        n = len(s)
        while l < n:
            r = l
            while s[r] != "#":
                r+=1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])
            l = r
        return res
                
