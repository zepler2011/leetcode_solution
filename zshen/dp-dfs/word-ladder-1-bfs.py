class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        atoz = 'abcdefghijklmnopqrstuvwxyz'
        currq, nextq = [start], []
        visited = set()
        cnt = 1
        
        while currq:
            word = currq.pop(0)
            for i in range(len(word)):
                for new in atoz:
                    if word[i] == new:
                        continue
                    newWord = word[:i] + new + word[i+1:]
                    if newWord in visited:
                        continue
                    if newWord == end:
                        cnt += 1
                        return cnt 
                    elif newWord in dict:
                        nextq.append(newWord)
                        visited.add(newWord)
            if not currq:
                currq,nextq = nextq,currq
                cnt += 1
        
        return cnt        
"""
1. how to remember the depth info?
    用两个queue 即可。
    currqueue
    nextqueue
    当currqueue为空时，交换curr, next 在那个时候层级+1
2. 成环 / 死循环怎么办？
    加一个哈希表或哈希集合？
    加在哪里？
"""