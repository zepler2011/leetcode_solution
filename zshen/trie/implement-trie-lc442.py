class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False


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
