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
        while r < n:
            if s[r] == "#":
                num = int(s[l:r])
                size = r + 1 + num
                res.append(s[r+1: size])
                l, r = size, size
            else:
                r+=1
        return res
                
