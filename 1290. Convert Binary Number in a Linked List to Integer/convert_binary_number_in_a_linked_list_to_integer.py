# T.C.->O(n)
# S.C.->O(1)
# For both Approaches

# Bit Manipulation
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        while head:
            # Bitwise left shift result by 1 (equivalent to multiplying by 2) and perform bitwise OR with the current node's value to append it to the binary number we are building.
            result = (result << 1) | head.val
            head = head.next
        return result


# Math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
