class Solution:
    def minOperations(self, n: int) -> int:
        res = n - 1
        for i in range(res-2, 0, -2):
            res += i
        return res
