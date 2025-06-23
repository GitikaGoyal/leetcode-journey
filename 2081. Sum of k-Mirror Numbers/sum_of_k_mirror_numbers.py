class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def convertToBaseK(self, num: int, k: int) -> str:
        if num == 0:
            return "0"
        res = ""
        while num > 0:
            res += str(num % k)
            num //= k
        return res[::-1]  # Reverse to get the correct base-k representation, didnt compulsory to reverse because palindrome function can check reversed string as well

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        L = 1  # Length of the decimal palindrome

        while n > 0:
            half_length = (L + 1) // 2
            min_num = 10 ** (half_length - 1)
            max_num = 10 ** half_length - 1

            for num in range(min_num, max_num + 1):
                first_half = str(num)
                second_half = first_half[::-1]
                if L % 2 == 0:
                    pal = first_half + second_half
                else:
                    pal = first_half + second_half[1:]

                pal_num = int(pal)
                base_k = self.convertToBaseK(pal_num, k)
                if self.isPalindrome(base_k):
                    total += pal_num
                    n -= 1
                    if n == 0:
                        break
            L += 1

        return total

# Time complexity:
# O(( (10)^(D/2) ) * D)

# Space complexity:
# O(D)
# where D=log(base 10)n
