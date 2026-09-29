class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # comparing current character with character in the past, therefore monotonic stack decreasing
        result = [0] * len(temperatures)
        stack = [] # keeps track of the index of the temperatures
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:# 38 > 30
                result[stack.pop()] = i - stack[-1]  # [1] # 30 is popped
            stack.append(i)  
        return result               

        
        