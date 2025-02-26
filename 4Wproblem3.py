N=int(input())
stair=[]
for i in range(N):
    stair.append(int(input()))
    
def max_scores(N,stair):
    if N==1:
        return stair[0]
    elif N==2:
        return stair[0]+stair[1]
    
    dp=[0]*N
    dp[0]=stair[0]
    dp[1]=stair[1]+stair[0]
    dp[2]=max(stair[0],stair[1])+stair[2]

    for i in range(3,N):
        dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]
    
    return dp[-1]

print(max_scores(N,stair))

#dp[i]=max(dp[i-2],dp[i-3]+stair[i-1])+stair[i]
