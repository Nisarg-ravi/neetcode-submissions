class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for num in s:
            count[num]=count.get(num,0)+1
        for num in t:
            if num not in count or count[num]==0:
                return False
            count[num]-=1
        return True