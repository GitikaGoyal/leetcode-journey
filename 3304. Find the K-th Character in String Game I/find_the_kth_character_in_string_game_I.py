#Optimized Bit Manipulation Approach
#T.C.->O(log k)
#S.C.->O(1)
class Solution:
    def kthCharacter(self, k: int) -> str:
        return string.ascii_lowercase[(k-1).bit_count()]

#Simulation Approach
#T.C.->O(k)
#S.C.->O(k)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word=[0]
        while len(word)<k:
            word.extend([(x+1)%26 for x in word])
        return chr(ord("a") + word[k-1])
