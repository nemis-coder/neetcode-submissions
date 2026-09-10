class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set()
        l = 0
        max_window_size = 0
        for r in range(len(s)):
            if s[r] not in current_chars:
                current_chars.add(s[r])
            else:
                max_window_size = max(max_window_size, len(current_chars))
                while(l<r and s[r] in current_chars):
                    current_chars.remove(s[l])
                    l+=1
                current_chars.add(s[r])
        max_window_size = max(max_window_size, len(current_chars))
        return max_window_size


