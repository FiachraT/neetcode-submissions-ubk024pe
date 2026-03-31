class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ""
        for s in strs:
           s = str(len(s)) + "#" + s
           new_strs += s
        return new_strs

    def decode(self, s: str) -> List[str]:
        # use a sliding window to find the number of digits
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#" :
                j+=1
            num = int(s[i:j])
            end = j + 1+ num
            res.append(s[j+ 1: end])
            i = end
        return res


                



