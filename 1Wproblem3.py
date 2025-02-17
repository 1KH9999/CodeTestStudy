T = int(input())
K = [int(input()) for i in range(T)]

def isEureka(Number):
    for i in range(1,50):
        for j in range(1,50):
            for l in range(1,50):
                if Number==i*(i+1)//2+j*(j+1)//2+l*(l+1)//2:
                    return 1
    return 0

for i in K:
    print(isEureka(i))
