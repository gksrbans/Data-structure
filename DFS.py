# 임의의 그래프 구현
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}


#print(graph)
#print(graph['A'])

for i in reversed(graph['A']):
    print(i)

def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        print(node, 'node임')
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node])) # 해당 노드의 자식들을 스택에 추가해줌.
            print(stack, '스택임')

    return visited

print(dfs(graph,'A'))

