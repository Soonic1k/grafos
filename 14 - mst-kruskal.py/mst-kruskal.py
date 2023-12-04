def kruskal(grafo, vertices):
    arestas = []
    for i in range(vertices):
        for j in range(vertices):
            if grafo[i][j] != 0:
                arestas.append([i, j, grafo[i][j]])

    arestas = sorted(arestas, key=lambda item: item[2])
    resultado = []
    subset = [-1] * vertices

    def encontrar_pai(i):
        if subset[i] == -1:
            return i
        return encontrar_pai(subset[i])

    def unir_subconjuntos(i, j):
        raiz_i = encontrar_pai(i)
        raiz_j = encontrar_pai(j)
        subset[raiz_i] = raiz_j

    for u, v, peso in arestas:
        raiz_u = encontrar_pai(u)
        raiz_v = encontrar_pai(v)

        if raiz_u != raiz_v:
            resultado.append([u, v, peso])
            unir_subconjuntos(raiz_u, raiz_v)

    return resultado


n, m = map(int, input().split())
grafo = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v, peso = map(int, input().split())
    grafo[u][v] = peso
    grafo[v][u] = peso  

# Execução do algoritmo de Kruskal
arvore_geradora_minima = kruskal(grafo, n)

print(arvore_geradora_minima)
