class TrieNode:
    def __init__ (self):
        self.leaf = False
        self.children = {chr(i+97):None for i in range(26)}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.children[ch]:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.leaf = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if not curr.children[ch]:
                return False
            curr = curr.children[ch]

        if curr.leaf:
            return True

        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not curr.children[ch]:
                return False
            curr = curr.children[ch]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)