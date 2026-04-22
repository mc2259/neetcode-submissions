class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlnum(c):
            return ord('a')<=ord(c)<=ord('z') or (ord('A')<=ord(c)<=ord('Z')
            ) or ord('0')<=ord(c)<=ord('9')


        left = 0
        right = len(s) - 1
        while (left < right):
            while left <right and not isAlnum(s[left]):
                left += 1

            while left <right and not isAlnum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left = left+1
            right = right -1
        return True
            

        

        
        