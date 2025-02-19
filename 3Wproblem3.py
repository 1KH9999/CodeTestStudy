T=int(input())
results = [] 

def dfs(baechu_field,i,j):

        if i+1<N and baechu_field[i+1][j]==1:
            baechu_field[i+1][j]=0
            dfs(baechu_field,i+1,j)
        if j+1<M and baechu_field[i][j+1]==1:
            baechu_field[i][j+1]=0
            dfs(baechu_field,i,j+1)

for _ in range(T):
    M,N,K=map(int,input().split())
    baechu_field = [[0] * (M) for _ in range(N)]
    for i in range(K):
        A,B=map(int,input().split())
        baechu_field[B][A]=1
    pestcount=0
    for i in range(N):
        for j in range(M):
            if baechu_field[i][j]==1:
                baechu_field[i][j]=0
                dfs(baechu_field,i,j)
                pestcount+=1
    results.append(pestcount)

print("\n".join(map(str, results)))