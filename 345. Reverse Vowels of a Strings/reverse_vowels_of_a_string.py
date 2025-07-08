#T.C.->O(n)
#S.C.->O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        new_s = list(s)
        i,j = 0,len(s)-1
        while i<=j:
            while i<j and s[i] not in vow:
                i+=1
            while i<j and s[j] not in vow:
                j-=1
            new_s[i],new_s[j] = new_s[j],new_s[i]
            i+=1
            j-=1
        return ''.join(new_s)
