class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def func(threshold: int) -> int:
            deletions = 0
            for frequency in frequencies:
                if frequency < threshold:
                    deletions += frequency
                # If frequency is greater than the threshold plus k, delete the excess
                elif frequency > threshold + k:
                    deletions += frequency - threshold - k
            return deletions
        frequencies = Counter(word).values()
        return min(func(threshold) for threshold in range(len(word) + 1))

  #T.C.->O(26^2)
  #S.C.->O(1)
