class Solution:
    def romanToInt(self, s: str) -> int:
        rmn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = []
        for i in s:
            if res == []:
                res.append(rmn[i])            
            elif res[-1] == 1:
                if i == 'V':
                    res.append(3)
                elif i == 'X':
                    res.append(8)
                else:
                    res.append(rmn[i])
            elif res[-1] == 10:
                if i == 'L':
                    res.append(30)
                elif i == 'C':
                    res.append(80)
                else:
                    res.append(rmn[i])
            elif res[-1] == 100:
                if i == 'D':
                    res.append(300)
                elif i == 'M':
                    res.append(800)
                else:
                    res.append(rmn[i])
            else:
                res.append(rmn[i])                
        return sum(res)
