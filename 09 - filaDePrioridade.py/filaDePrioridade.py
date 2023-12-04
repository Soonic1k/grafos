import numpy as np

def fila_vazia(Q):
    return np.all(Q == 0)

def insere(Q, i):
    Q[i] = 1
    return Q

def busca(Q, i):
    return Q[i]

def extraiMinimo(Q):
    minimo_indice = np.argmin(Q)
    Q[minimo_indice] = 0
    return minimo_indice, Q

def minimo(Q):
    minimo_indice = np.argmin(Q)
    return minimo_indice, Q

# Leitura da entrada
n, k = (int(tmp) for tmp in input().split(" "))
Q = np.zeros(n, dtype=int)
chaves = list (int(tmp) for tmp in input().split(" "))

for _ in range(k):
    linha = input().split()
    
    if len(linha) == 1:
        operacao = linha
    elif len(linha) == 2:
        operacao, j = linha

    if operacao == 'I':
        j = int(j)
        Q = insere(Q, j)
        print(Q.tolist())
    elif operacao == 'B':
        j = int(j)
        resultado = busca(Q, j)
        print(f"{resultado} {Q.tolist()}")
    elif operacao == 'E':
        indice, Q = extraiMinimo(Q)
        print(f"{indice} {chaves[indice]} {Q.tolist()}")
    elif operacao == 'M':
        indice, Q = minimo(Q)
        print(f"{indice} {chaves[indice]} {Q.tolist()}")
    elif operacao == 'V':
        resultado = fila_vazia(Q)
        print(f"{resultado} {Q.tolist()}")

