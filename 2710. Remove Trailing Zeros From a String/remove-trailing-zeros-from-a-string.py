class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for index in range(len(num), 0, -1):
            if num[index - 1] != '0':
                return num[:index]
