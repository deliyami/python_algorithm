INF = int(1e9)

# 모든 변의 정보 입력
sides = [
    ['A', 'B', 9],
	['A', 'C', 2],
    ['B', 'A', 9],
    ['B', 'C', 6],
    ['B', 'D', 3],
    ['B', 'E', 1],
    ['C', 'A', 2],
    ['C', 'B', 6],
    ['C', 'D', 2],
    ['C', 'F', 9],
    ['D', 'B', 3],
    ['D', 'C', 2],
    ['D', 'E', 5],
    ['D', 'F', 6],
    ['E', 'B', 1],
    ['E', 'D', 5],
    ['E', 'F', 3],
    ['E', 'G', 7],
    ['F', 'C', 9],
    ['F', 'D', 6],
    ['F', 'E', 3],
    ['F', 'G', 4],
    ['G', 'E', 7],
    ['G', 'F', 4],
]

# 최단 거리 값을 모두 무한으로 초기화
node = {
    'A': INF,
    'B': INF,
    'C': INF,
    'D': INF,
    'E': INF,
    'F': INF,
    'G': INF,
}

# 정점의 개수, 변의 개수를 입력
sides_len = len(sides)
node_len = len(node)

def bellman_ford(start):
    # 시작 정점에 대해서 초기화
    node[start] = 0
    # 전체 node_len - 1번을 반복
    for i in range(node_len):
        # 매 반복마다 '모든 변'을 확인한다.
        for j in range(sides_len):
            cur_node = sides[j][0]
            next_node = sides[j][1]
            edge_cost = sides[j][2]
            # 현재 변을 거쳐서 다른 정점로 이동하는 거리가 더 짧은 경우 갱신
            if node[cur_node] != INF and node[next_node] > node[cur_node] + edge_cost:
                node[next_node] = node[cur_node] + edge_cost
                # node_len번째에도 값이 갱신된다면 음수 순환이 존재
                if i == node_len - 1:
                    return True

    return False

# 벨만 포드 알고리즘 실행
negative_cycle = bellman_ford('A')

# 음수 순환이 존재하면 -1 출력
if negative_cycle:
    print("순환이 존재")
else:
    # 1번 정점을 제외한 다른 모든 정점으로 가기 위한 최단 거리를 출력
    for key, value in node.items():
        # 도달할 수 없는 경우, -1 출력
        if value == INF:
            print(key, '도달 할 수 없음')
        # 도달할 수 있으면 거리 출력
        else:
            print(key, value)