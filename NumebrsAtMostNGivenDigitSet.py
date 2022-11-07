class Solution:
    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)
        mem = [0] * K + [1]

        for i in range(K-1, -1, -1):

            for d in D:
                if d < S[i]:
                    mem[i] += pow(len(D), (K-i-1))
                elif d == S[i]:
                    mem[i] += mem[i+1]

        return mem[0] + sum(pow(len(D), i) for i in range(1, K))