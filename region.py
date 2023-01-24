class Solution(object):
    def removeOuterParentheses(self, s):
        res = ""
        c = 0
        for i in str(s):
            if i == '(':
                c+=1
                if c != 1:
                    res += i
            elif i == ')':
                c-=1
                if c != 0:
                    res += i

        return res
