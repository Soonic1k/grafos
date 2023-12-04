def prim(grafo, vertices, raiz):
    chave = [float('inf')] * vertices
    pai = [-1] * vertices
    visitado = [False] * vertices
    chave[raiz] = 0

    while True:
        min_chave = float('inf')
        u = -1

        for i in range(vertices):
            if not visitado[i] and chave[i] < min_chave:
                min_chave = chave[i]
                u = i

        if u == -1:
            break

        visitado[u] = True

        for v, w in grafo[u]:
            if not visitado[v] and w < chave[v]:
                chave[v] = w
                pai[v] = u

    return chave, pai

# Leitura da entrada
n, m, r = (int(tmp) for tmp in input().split(" "))
grafo = [[] for _ in range(n)]

for _ in range(m):
    u, v, peso = (int(tmp) for tmp in input().split(" "))
    grafo[u].append((v, peso))
    grafo[v].append((u, peso)) 

# Execução do algoritmo de Prim
chave, pai = prim(grafo, n, r)

print(chave)
print(pai)
