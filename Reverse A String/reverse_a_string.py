class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n - 1 
        half = n // 2
        
        while i < j:
            old_i = s[i]
            s[i] = s[j]
            s[j] = old_i
            i += 1
            j -= 1