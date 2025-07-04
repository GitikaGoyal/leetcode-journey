#Brute-Force
#T.C.->O(2^n)
#S.C.->O(2^n)
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        s = "a"
        for op in operations:
            if op == 0:
                s += s
            else:
                s += ''.join(chr((ord(c) - 96) % 26 + 97) if c != 'z' else 'a' for c in s)
        return s[k - 1]

#Optimal
#T.C.->O(n)
#S.C.->O(1)
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        k -= 1
        for i in range(len(operations)-1, -1, -1):
            half = float('inf') if i >= 60 else 1 << i
            if k >= half:
                k -= half
                shift += operations[i]
        return chr(ord('a') + shift % 26)
