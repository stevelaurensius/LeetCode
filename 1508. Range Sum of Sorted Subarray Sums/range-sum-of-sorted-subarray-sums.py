from itertools import accumulate


class Solution:
    def rangeSum(self, nums, n, left, right):
        result = list(accumulate(nums))
        for i in range(1, len(nums)):
            result.extend(accumulate(nums[i:]))
        result.sort()
        mod = 10**9 + 7
        return sum(result[left-1:right]) % mod

