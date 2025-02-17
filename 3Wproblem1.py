from collections import deque
N,M,V=map(int,input().split())
graph=[]
for i in range(M):
    graph.append(list(map(int,input().split())))

def dfs(connected_graph,start_node):
    need_visit,visited=list(),list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        #방문하지 않은 노드이면
        if node not in visited:
            #방문목록에 추가
            visited.append(node)
            #방문해야하는 목록에 딕셔너리 값들 추가
            need_visit.extend(reversed(connected_graph[node]))

    return visited
def bfs(connected_graph,start_node):
    queue = deque([start_node])  # 큐 사용
    visited = []
    
    while queue:
        node = queue.popleft()  
        if node not in visited:
            visited.append(node)
            queue.extend(connected_graph[node])

    return visited


def make_graph(graph):
    connected_graph = [[] for _ in range(N+1)]
    for i in range(M):
        A,B=graph[i]
        connected_graph[A].append(B)
        connected_graph[B].append(A)
    for a in connected_graph:
        a.sort()

    return connected_graph

connected_graph = make_graph(graph)

# DFS 탐색 실행
dfs_result = dfs(connected_graph, V)
bfs_result = bfs(connected_graph, V)

# 출력 (공백으로 구분된 노드 방문 순서)
print(" ".join(map(str,dfs_result)))
print(" ".join(map(str,bfs_result)))

