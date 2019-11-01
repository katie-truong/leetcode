def checkIfConnected(n, connections):
    d = {}
    for u, v in connections:
        if u not in d:
            d[u] = []
        d[u].append(v)
        if v not in d:
            d[v] = []
        d[v].append(u)

    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
        else:
            return
        for conn in d[node]:
            dfs(conn)

    dfs(0)

    if len(visited) == n:
        return True
    
    return False

print(checkIfConnected(4, [[0,1],[2,0],[1,3]]))
        
