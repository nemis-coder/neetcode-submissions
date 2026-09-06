class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_s  = ""
        for char_s in s:
            if char_s.isalnum():
                remove_s+=char_s.lower()
        print(remove_s)
        return remove_s == remove_s[::-1]
        