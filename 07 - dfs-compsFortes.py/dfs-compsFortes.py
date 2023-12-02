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

def dfs_instantes_transposto(grafo_transposto, n, finalizacao_original):
    descoberta = [-1] * n
    finalizacao_transposto = [-1] * n
    tempo = 1
    
    # Ordenar vértices pelo tempo de finalização decrescente
    vertices_ordenados = sorted(range(n), key=lambda x: finalizacao_original[x], reverse=True)
    
    for vertice in vertices_ordenados:
        if descoberta[vertice] == -1:
            tempo = dfs(grafo_transposto, vertice, tempo, descoberta, finalizacao_transposto)
    
    return descoberta, finalizacao_transposto

    
def print_resposta(descoberta, finalizacao):
    resposta = ""
    for vertice in range(2 * len(descoberta)):
        for i in range(len(descoberta)):
            if descoberta[i] == vertice + 1:
                resposta += f"({i}"
        for j in range(len(finalizacao)):
            if finalizacao[j] == vertice + 1:
                resposta += f"{j})"
        resposta += " "
    print(resposta)

n, m = map(int, input().split())
grafo = [[] for _ in range(n)]
grafo_transposto = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo_transposto[v].append(u)

descoberta, finalizacao = dfs_instantes(grafo, n)

descoberta_transposto, finalizacao_transposto = dfs_instantes_transposto(grafo_transposto, n, finalizacao)
print_resposta(descoberta_transposto, finalizacao_transposto)