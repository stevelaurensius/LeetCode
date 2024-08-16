class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left = 0
        right = 0
        result = []
        temp = ''
        for char in s:
            if char == '(':
                left += 1
                temp += '('
            elif char == ')':
                right += 1
                temp += ')'
            if left == right:
                result.append(temp[1:-1])
                temp = ''
        return ''.join(result)
