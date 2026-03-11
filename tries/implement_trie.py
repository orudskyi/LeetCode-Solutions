"""
Problem 208. Implement Trie (Prefix Tree)
Category: Tries
Link: https://neetcode.io/problems/implement-prefix-tree/question
Difficulty: Medium
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        

if __name__ == "__main__":
    prefixTree = PrefixTree()
    prefixTree.insert("dog")
    print(prefixTree.search("dog"))    # return true
    print(prefixTree.search("do"))    # return false
    print(prefixTree.startsWith("do")) # return true
    prefixTree.insert("do")
    print(prefixTree.search("do"))     # return true