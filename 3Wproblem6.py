from collections import deque
N,K=map(int,input().split())

def bfs(N,K):
    if N==K:
        return 0,1
    
    time=0
    queue=deque([N])
    visited=[-1]*100001
    visited[N]=0
    count=[0]*100001
    count[N]=1

    while queue:
        time += 1
        for _ in range(len(queue)):
            a = queue.popleft()
            
            next=[a*2,a+1,a-1]
            for next_pos in next:
                if 0<=next_pos<=100000:
                    if visited[next_pos] ==-1:
                        visited[next_pos]=visited[a]+1
                        count[next_pos]=count[a]
                        queue.append(next_pos)

                    elif visited[next_pos] == visited[a]+1:
                        count[next_pos] +=count[a]
        

    return visited[K],count[K]

time,count=bfs(N,K)
print(time)
print(count)

