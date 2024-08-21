class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = [x for x in nums if x % 3 != 0]
        return len(result)
