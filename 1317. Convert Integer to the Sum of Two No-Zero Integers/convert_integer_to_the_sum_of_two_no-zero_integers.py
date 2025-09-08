# Approach - I
# T.C.->O(nlogn)
# S.C.->O(1)
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(1, n):
            B = n - A
            if "0" not in str(A) + str(B):
                return [A, B]
        return []


# Approach - II
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(val):
            while val:
                tmp=val%10
                if tmp==0:
                    return False
                val//=10
            return True
        for a in range(1,n): 
            b=n-a
            if check(a) and check(b):
                return [a,b]turn ans;
    }
};
