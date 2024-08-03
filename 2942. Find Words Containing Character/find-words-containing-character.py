class Solution:
    def findWordsContaining(self, words, x):
        result = [index for index in range(len(words)) if x in words[index]]
        return result
