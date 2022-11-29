#User function Template for python3

class Solution:
    def numoffbt(self, arr, n):
     # Your code goes here
        maxvalue=max(arr)
        minvalue=min(arr)
        mark=[0]*(maxvalue+2)
        value=[0]*(maxvalue+2)
        for i in range(n):
            mark[arr[i]]=1
            value[arr[i]]=1
        ans=0
        mod=10**9+7
        for i in range(minvalue,maxvalue+1):
            if mark[i]:
                j=i+i
                while j<=maxvalue and (j//i)<=i:
                    if not mark[j]:
                        j+=i
                        continue
                    value[j]=(value[j]+(value[i]*value[j//i]))%mod
                    if i!=j//i:
                        value[j]=(value[j]+(value[i]*value[j//i]))%mod
                    j+=i
            ans=(ans+value[i])%mod
        return ans