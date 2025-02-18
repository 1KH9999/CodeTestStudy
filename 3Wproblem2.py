N,M=map(int,input().split())
graph=[]
for i in range(M):
    graph.append(list(map(int,input().split())))

def make_graph(graph):
    connected_graph = [[] for _ in range(N+1)]
    for i in range(M):
        A,B=graph[i]
        connected_graph[A].append(B)
        connected_graph[B].append(A)
    for a in connected_graph:
        a.sort()

    return connected_graph

def dfs(connected_graph,start_node):
    need_visit=list()
    visited=set()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        #방문하지 않은 노드이면
        if node not in visited:
            #방문목록에 추가
            visited.add(node)
            #방문해야하는 목록에 딕셔너리 값들 추가
            need_visit.extend(reversed(connected_graph[node]))

    return visited

connected_graph=make_graph(graph)
component_count=0
visited=[False]*(N+1)
for i in range(1,N+1):
    if not visited[i]:
        b=dfs(connected_graph,i)
        for a in b:
            visited[a]=True
        component_count+=1

print(component_count)
