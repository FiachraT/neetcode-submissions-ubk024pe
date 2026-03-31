class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map, keys are sorted word, value is the list of words
        groups = {}
        for w in strs:
            srt = "".join(sorted(w))
            groups.setdefault(srt, []).append(w)
        return list(groups.values())