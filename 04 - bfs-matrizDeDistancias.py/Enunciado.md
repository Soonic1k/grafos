Descrição

Faça um programa que faz a leitura de um grafo e imprime a matriz de distâncias obtidas por buscas em largura (BFS).



Entrada

Recebe n, m: n é o total de vértices, m o total de arcos.
A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime a matriz de distâncias obtidas por buscas BFS.



Exemplo

Entrada:

6 14
0 1
0 4
1 0
1 2
1 4
2 1
2 3
3 2
3 4
3 5
4 0
4 1
4 3
5 3
Saída: 
0: 0 1 2 2 1 3 
1: 1 0 1 2 1 3 
2: 2 1 0 1 2 2 
3: 2 2 1 0 1 1 
4: 1 1 2 1 0 2 
5: 3 3 2 1 2 0