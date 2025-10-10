#### Problem Statement
# You are at origin on number line and you have to reach n on number
# You are given an array that gives cost at each step from 1 to n
# Suppose if you stopped at step j you add arr[j] to the cost it takes to reach until that step j 
# Additionally you are given k which says how many steps you can take from a step

#### Solution using Dynamic Programming 

arr=[1,2,3,4]   # cost for step 1 =1 , step 2 =2, ..
k=2             # From each step you can take atmost 2 steps

#### Our main goal is to get the min cost to reach end 

#### Code
dp=[0]*(len(arr)+1)
dp[0]=0
dp[1]=arr[0]

for i in range(2,len(dp)):
    mini=float('-inf')
    for j in range(k):
        dp[i]=max(mini,dp[i-j-1]+arr[i-1])

print(dp)
print(dp[len(arr)])   # 6 which is minimum cost required to reach 5th step
        