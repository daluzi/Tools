class Solution:
    # def sumNums(self, n: int) -> int:
    #     return sum(range(n+1))
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res