# N=int(input())
# schedule=[]
# for i in range(N):
#     schedule.append(list(map(int,input().split())))
# revenue_predict=[]

# for i in range(len(schedule)):
#     if schedule[i][0] <= len(schedule)-i:
#         totalrevenue = schedule[i][1]
#         Counsel_day = schedule[i][0]
#         next_index=0
#         while next_index < len(schedule):
#             next_index = i + Counsel_day
#             if next_index >= len(schedule) or next_index+schedule[next_index][0]>len(schedule) :
#                 break
#             totalrevenue += schedule[next_index][1]
#             Counsel_day += schedule[next_index][0]
#         revenue_predict.append(totalrevenue)

# print(revenue_predict)

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

