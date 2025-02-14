from itertools import combinations
N=int(input())
ability_graph=[]
for i in range(N):
    ability_graph.append(list(map(int,input().split())))

# #0번 부터 N-1번까지의 선수 1,2를 가져가면 [0][1] [1][0]
# #1,2,4 가져가면 [0][1] [1][0] [0][3] [3][0] [1][3] [3][1]
# #3,5,6 [2][4] [4][2] [2][5] [5][2] [4][5] [5][4]

#0번부터 n-1 까지의 조합
def people_comb(n):
    people=list(range(n))
    comblist=list(combinations(people,n//2))

    return comblist

#1개 의 팀 조합에서 파워 출력
def ability_people(comb,ability_graph):
    duo_power=list(combinations(comb,2))
    teampower=0
    for a in duo_power:
        i,j=a
        teampower +=ability_graph[i][j]+ability_graph[j][i]

    return teampower

team_powerlist=[]
comblist=people_comb(N)
for comb in comblist:
    teampower=ability_people(comb,ability_graph)
    team_powerlist.append(teampower)
print(team_powerlist)

min_diff=float('inf')
diff_list=[]
M=len(team_powerlist)
for i in range(M-1):
    diff=abs(team_powerlist[i]-team_powerlist[M-i-1])
    diff_list.append(diff)
    if diff < min_diff:
        min_diff=diff
print(diff_list)
print(min_diff)