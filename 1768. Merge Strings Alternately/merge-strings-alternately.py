class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_1 = word1
        word_2 = word2
        if len(word_1) > len(word_2):
            word_2 = word_2 + (' ' * (len(word_1) - len(word_2)))
        elif len(word_2) > len(word_1):
            word_1 = word_1 + (' ' * (len(word_2) - len(word_1)))
        result = []
        for i in range(len(word_1)):
            result.append(word_1[i])
            result.append(word_2[i])
        return ''.join(result).replace(' ','')