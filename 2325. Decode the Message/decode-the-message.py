class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_ = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for i in key:
            if i == ' ':
                key_ = key_
            elif i not in key_:
                key_ += i

        for i in message:
            if i == ' ':
                result += ' '
            else:
                result += alphabet[key_.index(i)]
        return result
