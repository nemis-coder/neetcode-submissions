class WordDictionary:
    END = "#"

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.END] = True

    def dfs(self, node, word) -> bool :
        for ind,char in enumerate(word):
            if char in node:
                node = node[char]
            elif (char not in node) and (char!='.'):
                return False
            else:
                for candidate in node:
                    if candidate == self.END:
                        continue
                    if self.dfs(node[candidate],word[ind+1:]):
                        return True
                return False
        return self.END in node

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node,word)

                    