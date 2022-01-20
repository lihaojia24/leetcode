class TreeNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isEnd = False
    
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = TreeNode()
            node = node.children[index]
        node.isEnd = True 


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()


    def addWord(self, word: str) -> None:
        self.root.insert(word)


    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(index: int, node: TreeNode) -> bool:
            if index == n:
                return node.isEnd
            ch = word[index]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child and dfs(index + 1, child):
                        return True
            return False
        return dfs(0, self.root)





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)