class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = collections.defaultdict(int)
        window = collections.defaultdict(int)
        count =0
        l = 0
        resLen = float("inf")
        res = [-1, -1]

        for c in t:
            T[c] += 1
        need = len(T)
        for r, c in enumerate(s):
            window[c] += 1
            if c in T and window[c] == T[c]:
                count +=1
            while count == need:
                winLen = r - l + 1
                if winLen < resLen:
                    res = [l, r]
                    resLen = winLen
                window[s[l]] -= 1
                if s[l] in T and window[s[l]] < T[s[l]]:
                    count -=1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""


