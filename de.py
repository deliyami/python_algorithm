import heapq # 우선순위 큐 구현을 위함

INF = int(1e9)

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 6, 'D': 1, 'E': 3},
    'C': {'A': 5, 'B': 6, 'F': 8},
    'D': {'B': 1, 'E': 4},
    'E': {'B': 3, 'D': 4, 'G': 9,},
    'F': {'C': 8, 'G': 7},
    'G': {'E': 5, 'F': 7},
}

distances = {node: INF for node in graph} 

def dijkstra(graph, start):
    # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0
    queue = []
    # 시작 노드부터 탐색 시작 하기 위함
    heapq.heappush(queue, [distances[start], start])  

    # queue에 값이 남아 있는 동안 반복
    while queue:  
        # 탐색 할 노드, 거리를 가져옴
        current_distance, current_destination = heapq.heappop(queue)
         
        # 기존 거리보다 짧은지 확인
        if distances[current_destination] < current_distance:  
            continue

        for new_destination, new_distance in graph[current_destination].items():
            # 해당 노드를 거쳐 갈 때 거리
            distance = current_distance + new_distance
            # 기존 거리 보다 작으면 갱신
            if distance < distances[new_destination]:  
                distances[new_destination] = distance
            # 다음 인접 거리를 계산 하기 위해 큐에 삽입
            heapq.heappush(queue, [distance, new_destination])

    return distances

for key, value in dijkstra(graph, 'A').items():
    print(key, value)