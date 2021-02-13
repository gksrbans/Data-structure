# 모든 정점사이의 최소 cost를 통한 최단 경로를 찾는 탐색 알고리즘.

INF = 9876543210  # 무한대 정의

n = 4
a = [[0, 2, INF, 4], [2, 0, INF, 5], [3, INF, 0, INF], [INF, 2, 1, 0]]

def Floyd_Warshall():
    dist = [[INF] * n for i in range(n)]

    for i in range(n): # 최단 경로를 담는 배열 초기화
        for j in range(n):
            dist[i][j] = a[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist [k][j]

    return dist

dist = Floyd_Warshall()
print(dist)

for i in range(n):
    for j in range(n):
        print(dist[i][j], end='')
    print()


# [[0, 2, 5, 4], [2, 0, 6, 5], [3, 5, 0, 7], [4, 2, 1, 0]]
# 0254
# 2065
# 3507
# 4210