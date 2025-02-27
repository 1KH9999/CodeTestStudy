N=int(input())

# 1 2 3 5 8 13 21 34 55
square=[0]*(N+1)

square[1]=1
square[2]=2

for i in range(3,N+1):
    square[i]=square[i-2]+square[i-1]

print(square[N])