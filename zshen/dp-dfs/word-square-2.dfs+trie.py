class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            
        node.isWord = True
        node.word = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.root 
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
            
        return node.isWord 

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        
        node = self.root 
        
        for c in prefix:
            if c not in node.children:
                return False 
            node = node.children[c]
            
        return True 

    def find(self, prefix):
        node = self.root 
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        
        # dfs to find all words
        return self.dfs(node)

    def dfs(self, node):
        ret = []
        if node.isWord:
            ret.append(node.word)
        
        for c,node in node.children.items():
            ret.extend(self.dfs(node))
        return ret

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        if not words or not words[0]:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        results = []
        self.dfs(words, [], results, trie)
        return results
    
    def dfs(self, A, square, res, t):
        n = len(A[0])
        if len(square) == n:
            res.append(list(square))
            return
        
        if len(square) > n:
            return

        for w in self.getwords(A, square, t):
            square.append(w)
            self.dfs(A, square, res, t)
            square.pop()
        return

    def getwords(self, A, square, trie):
        n = len(square)
        m = len(A[0])
        prefix = ''.join([square[i][n] for i in range(n)])
        words = trie.find(prefix)

        if n+1 <= m:
            return words
            
        ret = []
        for w in words:
            new_square = square + [w]
            n = len(new_square)
            for j in range(n+1, m):
                new_prefix = ''.join([new_square[i][j] for i in range(n)])
                if not trie.startsWith(new_prefix):
                    break
                elif j == m-1:
                    ret.append(w)
        return ret
        

