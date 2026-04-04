class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window
        # Could be any character in the string
        # Append to each sequence of the letter and see which string is the longest?
        # Key insight. Window is valid if (window length - count of most frequent character <= k)
        l = 0
        count = {}
        max_freq = 0
        max_win = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            win = r - l + 1
            max_freq = max(max_freq, count[c])
            if win - max_freq <= k:
                max_win = max(max_win, win)
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
        return max_win
            



