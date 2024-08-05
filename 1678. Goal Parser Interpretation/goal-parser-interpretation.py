class Solution(object):
    def interpret(self, command):
        a = command.replace('()', 'o')
        b = a.replace('(al)', 'al')
        return b
