
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
        
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        node = self.root 
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode
            node = node.children[c]
            
        node.isWord = True 

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        return self.helper(self.root, word)
        
    def helper(self, node, s):
        if not s:
            return node.isWord

        c = s[:1]
        if c != '.':
            if c in node.children:
                n = node.children[c]
                return self.helper(n, s[1:])
            else:
                return False
        else:
            for _,n in node.children.items():
                if self.helper(n, s[1:]):
                    return True
            return False
