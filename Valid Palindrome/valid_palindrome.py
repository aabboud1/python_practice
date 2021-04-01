class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = []
        
        for x in s:
            if (ord(x) > 64 and ord(x) < 91) or (ord(x) > 96 and ord(x) < 123) or (ord(x) > 47 and ord(x) < 58):
                new_string.append(x.lower())
        
        n = len(new_string)
        
        half = n // 2
        
        for x in range(half):
            if new_string[x] != new_string[n - 1 - x]:
                return False
        return True