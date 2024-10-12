class Solution:
    def rangeSum(self, A, B):
        numLength = len(A)
        anss = [0 for i in range(len(B))]


        prefix_sum = [0 for i in range(numLength)]
        prefix_sum[0] = A[0]

        for i in range(1, numLength):
            prefix_sum[i] = prefix_sum[i - 1] + A[i]

        for i in range(len(B)):
            L = B[i][0]
            R = B[i][1]
            if L  == 0:
                anss[i] = prefix_sum[R]
            else:
                anss[i] = prefix_sum[R] - prefix_sum[L-1]
        
        return anss


        
A = [-2, 0, 3, -5, 2, -1]

B = [[0,2], [2,5], [0,5]]

s = Solution()
print(s.rangeSum(A,B))


# //list comprehension
