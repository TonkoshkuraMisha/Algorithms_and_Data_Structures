"""
Обход в глубину. DFS.
"""
def dfs(vertex, G, used):
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs(neighbor, G, used)

used = {}
N = 0
for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1
print(N)


# Алгоритм Косорайю. Поиск компонент сильной связности.

# Топологическая сортировка. Алгоритм Тарьяна. Алгоритм Прима.
u = []
visited = [False]*(n+1)
ans = []
def dfs(start, G, visited, ans):
    visited[start] = True
    for u in G[start]:
        if not visited[n]:
            dfs(u, G, visited, ans)
    ans.append(start)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, G, visited, ans)
ans[:] = ans[::-1]


