class Solution:
    def maxDepth(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                temp = left - right
                if temp >= result:
                    result = temp
                right += 1
        return result
