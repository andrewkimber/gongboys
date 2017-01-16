V = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

adj = {
    'a': ['c'],
    'b': ['c', 'd'],
    'c': ['e'],
    'd': ['f'],
    'e': ['f', 'h'],
    'f': ['g'],
    'g': [],
    'h': []
}

parent={'a':None}
def DFS_visit(V, adj, s):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_visit(V, adj, v)


def DFS(V, adj):
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(V, adj, s)


DFS(V,adj)
print parent
