def dfs (grafo, vertice, tempo, descoberta, finalizacao):
    descoberta[vertice] = tempo
    tempo += 1
    
    for vizinho in grafo[vertice]:
        if descoberta[vizinho] == -1:
            tempo = dfs(grafo, vizinho, tempo, descoberta, finalizacao)
    
    finalizacao[vertice] = tempo
    tempo += 1
    
    return tempo

def dfs_instantes(grafo, n):
    descoberta = [-1] * n
    finalizacao = [-1] * n
    tempo = 1
    
    for vertice in range(n):
        if descoberta[vertice] == -1:
            tempo = dfs(grafo, vertice, tempo, descoberta, finalizacao)
    
    return descoberta, finalizacao

def print_grafo(descoberta, finalizacao):
    print(descoberta)
    print(finalizacao)     

def ler_grafo():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        grafo[u].append(v)

    return grafo, n

grafo, n = ler_grafo()
descoberta, finalizacao = dfs_instantes(grafo, n)
print_grafo(descoberta, finalizacao)
