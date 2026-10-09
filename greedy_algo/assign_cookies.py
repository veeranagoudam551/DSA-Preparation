class Solution(object):
    def findContentChildren(self, g, s):
        i=0
        j=0
        s.sort()
        g.sort()

        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                i+=1
            j+=1
        return i