import numpy as np

def insere(Q, i):
    Q[i] = 1
    return Q

def busca(Q, i):
    return Q[i]

def extraiMinimo (Q, chave):
    for i in range (len(Q)):
        if Q[i] == 1:
            min = i
            break
    for i in range (len(Q)):
        if Q[i] == 1  and chave[i] < chave[min]:
            min = i
    Q[min] = 0
    return min, Q 

def minimo(Q, chave):
    for i in range (len(Q)):
        if Q[i] == 1:
            min = i
            break
    for i in range (len(Q)):
        if Q[i] == 1  and chave[i] < chave[min]:
            min = i
    return min

def fila_vazia (Q):
    for i in range (len(Q)):
        if Q[i] == 1:
            return False
    return True


# Leitura da entrada
n, k = (int(tmp) for tmp in input().split(" "))
Q=[0]*n
tmp2 = list (int(tmp) for tmp in input().split(" "))
chave = np.array (tmp2)

for _ in range(k):
    linha = input().split()
    
    if len(linha) == 1:
        operacao = linha[0]
    elif len(linha) == 2:
        operacao, j = linha

    if operacao == 'I':
        Q=insere(Q, int(j))
        print(Q)
    elif operacao == 'B':
        resultado = busca(Q, int(j))
        print(resultado, Q)
    elif operacao == 'E':
        min, Q =extraiMinimo(Q, chave)
        print(min, chave[min], Q)
    elif operacao == 'M':
        min=(minimo(Q, chave))
        print(min, chave[min], Q)
    elif operacao == 'V':
        resultado = fila_vazia(Q)
        print(resultado, Q)