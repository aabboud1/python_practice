class Solution:
    def isPalindrome(self, s: str) -> bool:
        # New list of alphanumeric charcters only
        new_string = []
        
        # Use ASCII codes to check if character is alphanumeric then append to the new list
        for x in s:
            # checks if alpha numeric
            if (ord(x) > 64 and ord(x) < 91) or (ord(x) > 96 and ord(x) < 123) or (ord(x) > 47 and ord(x) < 58):
                new_string.append(x.lower())
        
        #Get length of the string
        n = len(new_string)
        
        # Get half of the string and take floor
        half = n // 2
        
        # check if palindrome
        for x in range(half):
            if new_string[x] != new_string[n - 1 - x]:
                return False
        return True