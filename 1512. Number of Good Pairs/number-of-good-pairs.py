class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = [(x,y) for x in range(len(nums)) for y in range(len(nums)) 
        if nums[x] == nums[y] and x < y]
        return len(result)
