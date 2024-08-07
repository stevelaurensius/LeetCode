class Solution:
    numberText = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
        19: 'Nineteen', 20: 'Twenty',
        30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
        100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'
    }

    def numberToWords(self, n):
        if n == 0:
            return 'Zero'
        result = ''

        for num in sorted(self.numberText.keys(), reverse=True):
            count = int(n/num)
            if (count < 1):
                continue
            if (num >= 100):
                result += self.numberToWords(count) + ' '
            result += self.numberText[num]
            n -= count * num
            if (n > 0):
                result += ' '
        return result