class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      if len(s1) > len(s2): return False
      s1_check = [0] *26
      s2_check = [0] *26
      for i in range(len(s1)):
        s1_check[ord(s1[i]) - ord('a')] += 1
        s2_check[ord(s2[i]) - ord('a')] += 1
     
      matches = 0
      for i in range(26):
        if s1_check[i] == s2_check[i]:
            matches +=1

      l = 0
      for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        indx = ord(s2[r]) - ord('a')
        s2_check[indx] += 1
        if s2_check[indx] == s1_check[indx]:
            matches +=1
        elif s2_check[indx] - 1 == s1_check[indx]:
            matches -=1
        
        indx = ord(s2[l]) - ord('a')
        s2_check[indx] -= 1
        if s2_check[indx] == s1_check[indx]:
            matches +=1
        elif s2_check[indx] + 1 == s1_check[indx]:
            matches -=1
        
        l += 1
      return matches ==26

    