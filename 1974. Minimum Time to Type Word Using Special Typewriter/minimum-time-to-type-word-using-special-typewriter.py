class Solution:
    def minTimeToType(self, word: str) -> int:
        result = len(word)
        pointer = 97
        for i in word:
            diff = abs(ord(i) - pointer)
            result += min(diff, 26 - diff)
            pointer = ord(i)
        return result
