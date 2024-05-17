class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        "121"
        "y=1"
        "temp = 12"
        y = 0
        temp = x
    
        while temp:
            y = (y * 10) + (temp % 10)
            temp //= 10
    
        return x == y
        
