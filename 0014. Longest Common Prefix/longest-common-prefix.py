class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        checker = strs[0]
        if checker == '':
            return ''
        for char in range(1, len(checker)+1):
            check_word = checker[:char]
            for word in strs:
                if not word.startswith(check_word):
                    return checker[:char-1]
        return check_word
