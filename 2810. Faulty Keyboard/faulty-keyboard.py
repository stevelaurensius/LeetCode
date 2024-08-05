class Solution:
    def finalString(self, s: str) -> str:
        result_ = ''
        for i in s:
            if i == 'i':
                result_ = result_[::-1]
            else:
                result_ += i
        return result_
