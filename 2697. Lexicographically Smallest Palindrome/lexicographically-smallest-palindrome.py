class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        word = list(s)
        for i in range((len(word) // 2)):
            left = i
            right = (i+1) * -1
            if ord(word[left]) > ord(word[right]):
                word[left] = word[right]
            else:
                word[right] =  word[left]
        return ''.join(word)