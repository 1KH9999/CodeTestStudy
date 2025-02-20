import sys

sys.setrecursionlimit(10000)

N = int(input())  # 정사각형 지도 크기
grid = [list(map(int, input().strip())) for _ in range(N)]  # 지도 입력

def dfs(x, y):
    global count
    grid[x][y] = 0  # 방문 처리
    count += 1  # 현재 단지 내 집 개수 증가

    if y+1<N and grid[x][y+1]==1:
        dfs(x,y+1)
    if x+1<N and grid[x+1][y]==1:
        dfs(x+1,y)
    if y-1>=0 and grid[x][y-1]==1:
        dfs(x,y-1)
    if x-1>=0 and grid[x-1][y]==1:
        dfs(x-1,y)

complex_sizes = []  # 단지 내 집 개수를 저장할 리스트
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:  # 집이 있는 경우
            count = 0
            dfs(i, j)
            complex_sizes.append(count)

# 결과 출력
print(len(complex_sizes))  # 총 단지 수
print("\n".join(map(str, sorted(complex_sizes))))  # 오름차순 정렬 후 출력
