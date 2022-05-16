from collections import deque

# 모든 정점과 해당 정점과 연결된 정점의 정보 입력
node_list = {'A': set(['B','C','D']),
              'B': set(['E','F']),
              'C': set(['H']),
              'D': set(['I','J']),
              'E': set(['K']),
              'F': set([]),
              'H': set(['G']),
              'I': set([]),
              'J': set(['L']),
              'K': set([]),
              'G': set([]),
              'L': set([]),}

# 시작 정점
root_node = 'A'

# 도착 정점
check_node = 'G'

def BFS_with_adj_list(graph, root):
		# 방문한 정점에 대해서 초기화
    visited = []
    queue = deque([root])
		# queue에 값이 없을 때 까지 반복
    while queue:
				# queue에 들어있는 값을 꺼내오고 도착 정점과 같은지 확인
        n = queue.popleft()
        if check_node == n:
            return n
				# 현재 정점을 확인
        print('this node:',n)
				# 현재 정점을 방문 한 적이 없다면 현재 정점에 연결된 정점을 queue에 삽입
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    
# BFS 실행
print(BFS_with_adj_list(node_list, root_node))