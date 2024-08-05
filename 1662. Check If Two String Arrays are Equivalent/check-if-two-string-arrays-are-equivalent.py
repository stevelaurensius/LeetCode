class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        first = [j for i in word1 for j in i]
        second = [j for i in word2 for j in i]
        result = True if first == second else False
        return result
