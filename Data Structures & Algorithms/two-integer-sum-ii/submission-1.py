class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input will always be valid
        # index1 always less than index two
        # Almost certainly O(N)
        #Can't use hash map because only alllowed to us O(1) addidtional space
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -=1
            else:
                l += 1
            

