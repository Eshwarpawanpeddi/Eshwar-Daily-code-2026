class Solution:
    def isPalindrome(self, x: int) -> bool:
        if -2**31 <= x <= 2**31 - 1:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False