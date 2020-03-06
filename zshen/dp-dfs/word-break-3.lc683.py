class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        # ignore cases
        new_dict = []
        for d in dict:
            new_dict.append(d.lower())
        s = s.lower()
        
        n = len(s)
        f = [0] * (n+1)
        f[0] = 1
        
        for i in range(n+1):
            for j in range(i):
                if s[j:i] in new_dict:
                    f[i] += f[j]
                    
        return f[n]

"""
1. state: f[i] := # how many ways:
2. fang cheng: f[i] = sum(f[j] | s[i..j] in dict for j in range(i))
3. bian jie: f[0] = 1 
4. ans:  f[n]
"""