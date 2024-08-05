import re


class Solution:
    def countConsistentStrings(self, allowed, words):
        pattern = r'^[' + re.escape(allowed) + r']+$'
        result = len([x for x in words if bool(re.match(pattern, x))])
        return result