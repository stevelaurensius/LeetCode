class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for index in range(len(word)):
            if word[index] == ch:
                return (word[:index+1][::-1] + word[index + 1:])
        return word
