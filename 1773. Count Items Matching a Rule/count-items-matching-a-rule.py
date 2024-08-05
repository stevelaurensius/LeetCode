class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        if ruleKey == 'type':
            result = len([item for item in items if ruleValue == item[0]])
            return result
        elif ruleKey == 'color':
            result = len([item for item in items if ruleValue == item[1]])
            return result
        elif ruleKey == 'name':
            result = len([item for item in items if ruleValue == item[2]])
            return result
