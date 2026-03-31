class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string
        

    def decode(self, s: str) -> List[str]:
        #Sliding window to get number first, then slicing to get remaining characters
        # Make sure not to make out of bound calls with array
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            i =  j + 1 + num
            arr.append(s[j + 1: i])
        return arr


