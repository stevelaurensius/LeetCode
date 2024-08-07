class Solution:
    def replaceDigits(self, s: str) -> str:
        result = [x for x in s]
        for i in range(len(result)):
            if result[i].isdigit():
                result[i] = chr(ord(result[i - 1]) + int(result[i]))
        return ''.join(result)