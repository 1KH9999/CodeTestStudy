from collections import deque
N=int(input())

def bfs_search(N):
    queue=deque([(N,0)])
    visited=set()
    visited.add(N)
    
    while queue:
        a , count=queue.popleft()

        if a==1:
            return count
        if a%3==0  and a // 3 not in visited:
            queue.append((a//3,count+1))
            visited.add(a//3)
        if a%2==0 and a // 2 not in visited:
            queue.append((a//2,count+1))
            visited.add(a//2)
        if a - 1 not in visited:
            queue.append((a-1,count+1))
            visited.add(a-1)
print(bfs_search(N))