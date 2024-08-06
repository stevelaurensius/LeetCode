class Solution:
    def minimumPushes(self, word):
        word_set = sorted([word.count(x) for x in set(word)], reverse=True)
        result = 0
        for counter in range(1, len(word_set) + 1):
            if counter <= 8:
                result += (word_set[counter - 1] * 1)
            elif counter <= 16:
                result += (word_set[counter - 1] * 2)
            elif counter <= 24:
                result += (word_set[counter - 1] * 3)
            elif counter > 24:
                result += (word_set[counter - 1] * 4)
        return result
