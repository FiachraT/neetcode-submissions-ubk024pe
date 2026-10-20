class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0
        def count_palindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            # Add odd-length palindromes (centered at i)
            total_count += count_palindromes(i, i)
            # Add even-length palindromes (centered between i and i + 1)
            total_count += count_palindromes(i, i + 1)
        return total_count
        