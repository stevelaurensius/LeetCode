class Solution:
    def freqAlphabets(self, s: str) -> str:
        reversed_string = s[::-1]
        result = []
        while True:
            if len(reversed_string) == 0:
                break
            if reversed_string[0].isnumeric():
                result.insert(0, chr(96 + int(reversed_string[0])))
                reversed_string = reversed_string[1:]
            elif reversed_string[0] == '#':
                result.insert(0, chr(96 + int(reversed_string[2:0:-1])))
                reversed_string = reversed_string[3:]
        return ''.join(result)
