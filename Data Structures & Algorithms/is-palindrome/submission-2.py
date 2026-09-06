class Solution:
    def evaluatePalindSt(self, s:str)-> bool:
        return s==s[::-1]
    def isPalindrome(self, s: str) -> bool:
        remove_s  = ""
        for char_s in s:
            if char_s.isalnum():
                remove_s+=char_s.lower()
        return self.evaluatePalindSt(remove_s)
        