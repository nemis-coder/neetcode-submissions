class Solution:
    def encode(self, strs: List[str]) -> str:
        code_words = []
        for word in strs:
            size = len(word)
            encode_word = str(size) + "#" + word
            code_words.append(encode_word)
        return ''.join(code_words)

    def decode(self, s: str) -> List[str]:
        ind  = 0
        words = []
        while(ind<len(s)):
            current_size = ''
            while(s[ind]!="#"):
                current_size+= s[ind]
                ind +=1
            size = int(current_size)
            start_word = ind + 1
            end_word = start_word + size
            current_word = s[start_word:end_word]
            words.append(current_word)
            ind = end_word
        return words

