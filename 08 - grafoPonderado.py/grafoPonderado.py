n, m = map(int, input().split())

matriz = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, peso = map(int, input().split())
    matriz[i][j] = peso

for i in range(n):
    texto = f"{i}: "
    for j in range(n):
        if matriz[i][j] != 0:
            texto += f"{j}({matriz[i][j]})"
    print(texto)