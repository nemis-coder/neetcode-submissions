class Solution:
    def evaluatePalindIt(self, s:str)-> bool:
        for i in range(0,len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def evaluatePalindSt(self, s:str)-> bool:
        return s==s[::-1]

    def isPalindrome(self, s: str) -> bool:
        remove_s  = ""
        for char_s in s:
            if char_s.isalnum():
                remove_s+=char_s.lower()
        return self.evaluatePalindIt(remove_s)
        