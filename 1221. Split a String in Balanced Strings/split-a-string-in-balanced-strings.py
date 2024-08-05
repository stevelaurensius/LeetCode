class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        for i in s:
            right += 1 if i == 'R' else 0
            left += 1 if i == 'L' else 0
            if left == right:
                result += 1
        return result
