Bingoboard=[]
for i in range(5):
    Bingoboard.append(list(map(int,input().split())))

Numbers=[]
for i in range(5):
    Numbers.extend(map(int, input().split()))


def Bingo(Bingoboard):
    count=0
    #가로줄 빙고
    for i in range(5):
        if all(Bingoboard[i][j] == 0 for j in range(5)):  
            count += 1
    #세로줄 빙고
    for i in range(5):
        if all(Bingoboard[j][i] == 0 for j in range(5)):  
            count += 1
    #대각선 빙고
    if all(Bingoboard[i][i] == 0 for i in range(5)):  
        count+=1
    if all(Bingoboard[i][4-i] == 0 for i in range(5)):  
        count+=1     

    return count

found = False
for a in range(len(Numbers)):
    for i in range(5):
        for j in range(5):
            if Bingoboard[i][j] == Numbers[a]:
                Bingoboard[i][j] = 0  # 숫자 찾으면 0으로 변경
                if Bingo(Bingoboard) >= 3: 
                    find = a+1
                    found = True
                    break
        if found:
            break
    if found:
        break
print(find)