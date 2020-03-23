class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        res = []
        for word in words:
            if self.isMatch(pattern, word, {}, {}):
                res.append(word)
            
        return res 
    
    def isMatch(self, p, w, mapping, used):
        
        for i in range(len(w)):
            if p[i] not in mapping and w[i] not in used:
                mapping[p[i]] = w[i]
                used[w[i]] = p[i]
                continue 
                
            if p[i] in mapping:
                if mapping[p[i]] == w[i]:
                    continue
                else:
                    return False 
                            
            if w[i] in used:
                if used[w[i]] == p[i]:
                    continue
                else:
                    return False

        return True 