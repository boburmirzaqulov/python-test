class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.is_palindrome(s):
            return True

        for n in range(len(s)):
            if n < len(s)-1:
                str = s[:n] + s[n+1:]
                if self.is_palindrome(str):
                    return True

        return self.is_palindrome(s[:len(s)-1])
    def is_palindrome(self, s):
        return s==s[::-1]
