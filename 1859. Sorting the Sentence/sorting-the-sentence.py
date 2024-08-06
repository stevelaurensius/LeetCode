class Solution:
    def sortSentence(self, s):
        a = sorted(s.split(), key=lambda x :int(x[-1]))
        result = [x[:-1] for x in a]
        return ' '.join(result)