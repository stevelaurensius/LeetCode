class Solution:
    def findComplement(self, num: int) -> int:
        num_in_bin = bin(num)[2:]
        result = ''
        for i in num_in_bin:
            if i == '1':
                result += '0'
            else:
                result += '1'
        return int(result, 2)
