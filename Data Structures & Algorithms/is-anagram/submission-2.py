class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            l='abcdefghijklmnopqrstuvwxyz'
            for c in l:
               if s.count(c)!=t.count(c):
                return False
        return True