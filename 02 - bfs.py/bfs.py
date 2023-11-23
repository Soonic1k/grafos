# Assume que Q eh uma lista
def insere (Q, x):
    Q.append (x)

# Assume que Q nao eh vazio
def remove (Q):
    return Q.pop (0)

def vazio (Q):
    return len (Q) == 0

n, m, s = (int(tmp) for tmp in input().split(" "))
adj = [[] for _ in range(n)]
for k in range(m):
    i, j = (int(tmp) for tmp in input().split(" "))
    adj[i].append(j)

# algoritmo BFS

# inicializacao
d = [0] * n
cor = [0] * n
INF = 999999
BRANCO = 1
CINZA = 2
PRETO = 3
for v in range (n):
    d[v] = INF
    cor[v] = BRANCO
d[s] = 0

Q = [s]

while not vazio (Q):
    u = remove (Q)
    for v in adj[u]:
    if cor[v] == BRANCO:
        d[v] = d[u] + 1
        cor[v] = CINZA
        insere (Q, v)
    cor[u] = PRETO

texto = "%d: " % s

for i in d:
    texto += "%d " % i

print (texto)