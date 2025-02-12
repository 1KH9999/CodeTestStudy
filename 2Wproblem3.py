Bingoboard=[]
for i in range(5):
    Bingoboard.append(list(map(int,input().split())))

Numbers=[]
for i in range(5):
    Numbers.extend(map(int, input().split()))
count=0

def Bingo(Bingoboard):
    global count
    #가로줄 빙고
    for i in range(5):
        rowcount=0
        for j in range(5):
            if Bingoboard[i][j]==0:
                rowcount+=1
        if rowcount==5:
            count+=1
    #세로줄 빙고
    for i in range(5):
        columncount=0
        for j in range(5):
            if Bingoboard[j][i]==0:
                columncount+=1
        if columncount==5:
            count+=1
    #대각선 빙고
    for i in range(5):
        if Bingoboard[i][i]==0:
            count+=1
        elif Bingoboard[i][4-i]==0:
            count+=1
found=False
for number in Numbers:
    for i in range(5):
        for j in range(5):
            if Bingoboard[i][j]==number:
                Bingoboard[i][j]=0
            Bingo(Bingoboard)
            if count==3:
                find=(i)*5+j+1
                found=True
                break
        if found:        
            break
    if found:
        break
print(find)