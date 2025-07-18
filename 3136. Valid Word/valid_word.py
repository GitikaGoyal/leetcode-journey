# One Time Traversal
# T.C.->O(n)
# S.C.->O(1)

class Solution:
    def isValid(self, word: str) -> bool:
        if(len(word)>=3):
            has_vowel = False
            has_consonant = False
            for c in word:
                if c.isalpha():
                    if c.lower() in 'aeiou':
                        has_vowel=True
                    else:
                        has_consonant = True
                elif not c.isdigit():
                    return False
            return has_vowel and has_consonant
        else:
            return False
