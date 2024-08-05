class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=str(x)
        b=c[::-1]
        if c==b:
            return True
        else:
            return False
