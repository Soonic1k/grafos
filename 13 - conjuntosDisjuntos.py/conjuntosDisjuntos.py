def findSet (S, x):
    for i in range (len(S)):
        for j in S[i]:
            if j == x:
                return i    

def makeSet (S, x):
    S.append([x])

def union (S, x, y):
    i = findSet (S, x)
    j = findSet (S, y)
    S[i] += S[j]
    S[j].clear()


n = int(input())
S = []

for _ in range(n):
    linha = input().split()

    if len(linha) == 2:
        operacao, i = linha
        b = None  # Não há terceiro argumento
    elif len(linha) == 3:
        operacao, i, j = linha

    if operacao == 'M':
        makeSet(S, i)
        print(S)
    elif operacao == 'U':
        union (S, i, j)
        print(S)
    elif operacao == 'F':
        posicao = findSet(S, i)
        resposta = f"{posicao} {S}"
        print(resposta)