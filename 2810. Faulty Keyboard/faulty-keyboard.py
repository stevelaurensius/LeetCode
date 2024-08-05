class Solution:
    def finalString(self, s: str) -> str:
        result_ = ''
        for i in s:
            if i != 'i':
                result_ += i
            else:
                result_ = result_[::-1]
        return result_
