N,M=map(int,input().split())
rectangle=[]
for i in range(N):
    rectanglerow=[]
    row=input()
    for j in row:
        rectanglerow.append(j)
        rectangle.append(rectanglerow)

def findsquare(rectangle,N,M):
    for row in rectangle:
        lastseen={}
        diffsave={}
        for i,num in enumerate(row):
            if num in lastseen:
                diff=i-lastseen[num]
                diffsave[num]=i
            else:
                lastseen[num]=i

                
            