"""
Problem 212. Word Search II
Category: Tries
Link: https://neetcode.io/problems/search-for-word-ii/question
Difficulty: Hard
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]

            if node.word:
                res.add(node.word)
                node.word = None

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return list(res)


if __name__ == "__main__":
    solver = Solution()
    board = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"],
    ]
    
    words = ["bat","cat","back","backend","stack"]
    
    result = solver.findWords(board, words)
    
    print(f"Result: {result}")
