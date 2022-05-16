graph_list = {'A': set(['B','C','D']),
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
root_node = 'A'
check_node = 'G'

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]
    find_node = ''
    while stack:
        n = stack.pop()
        if check_node == n:
            find_node = n
            break
        print('this node:',n)
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return find_node

print(DFS_with_adj_list(graph_list, root_node))

