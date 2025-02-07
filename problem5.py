M,N=map(int,input().split())
originboard=[]
for i in range(M):
    originrow=[]
    colorstr=input()
    for j in colorstr:
        originrow.append(j)
    originboard.append(originrow)
        
def changeforchess(boardcut):
    pattern1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] * 4
    pattern2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] * 4
    
    diff1=0
    diff2=0

    for i in range(8):
        for j in range(8):
            if boardcut[i][j]!=pattern1[i][j]:
                diff1+=1
            elif boardcut[i][j]!=pattern2[i][j]:
                diff2+=1
    return min(diff1, diff2)
minchange=[]
for i in range(M-7):
    for j in range(N-7):
        boardcut=[row[j:j+8] for row in originboard[i:i+8]]
        minchange.append(changeforchess(boardcut))

minchange.sort()
print(minchange[0])