N=int(input())
schedule=[]
for i in range(N):
    schedule.append(list(map(int,input().split())))
dp=[0]*(N+1)
for i in range(N - 1, -1, -1):
    T, P = schedule[i]  # 상담 기간, 보상

    if i + T <= N:  # 상담 가능
        dp[i] = max(dp[i + 1], P + dp[i + T])
    else:  # 상담 불가능
        dp[i] = dp[i + 1]
print(dp)
print(dp[0])

