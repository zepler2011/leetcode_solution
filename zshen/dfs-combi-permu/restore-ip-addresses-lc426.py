class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        if not s:
            return []
            
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, ips, res):
        if len(ips) == 4 and not s:
            res.append('.'.join(ips))
            return
        if not s or len(ips)==4:
            return
        
        #if s[0] == '0':
        #    return 

        ips.append(s[:1])
        self.dfs(s[1:], ips, res)
        ips.pop()
            
        if len(s) > 1 and not s.startswith('0') and not s.startswith('00'):
            ips.append(s[:2])
            self.dfs(s[2:], ips, res)
            ips.pop()

            if len(s)>2 and int(s[:3])<256 and not s.startswith('000'):
                ips.append(s[:3])
                self.dfs(s[3:], ips, res)
                ips.pop()
            
        return