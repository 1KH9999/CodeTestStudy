from collections import deque
N,K=map(int,input().split())

def bfs(N,K):
    if N==K:
        return 0
    
    time=0
    queue= deque([N])

    while queue:
        time+=1
        for _ in range(len(queue)):
            a=queue.popleft()
            
            next=[a*2,a+1,a-1]
            for next_pos in next:
                if next_pos == K:
                    return time
                else:
                    queue.append(next_pos)

    return time

print(bfs(N,K))

        