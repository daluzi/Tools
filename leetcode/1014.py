class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        length = len(A)
        p = 0
        a = A[0] + 0
        for j in range(1, length):
            p = max(p , a + A[j] - j)
            a = max(a, A[j] + j)
        return p