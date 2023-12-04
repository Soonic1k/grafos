Descrição

Faça um programa que leia um grafo ponderado e calcule uma árvore geradora mínima pelo algoritmo de Kruskal.



Entrada

Recebe n, m; n é o total de vértices, m o total de arcos.
A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime a lista das arestas na ordem de inserção pelo algoritmo de Kruskal (i, j, peso).

Exemplo1

Entrada:

6 16
0 1 4
1 0 4
0 4 8
4 0 8
1 4 11
4 1 11
1 2 8
2 1 8
2 3 6
3 2 6
2 5 2
5 2 2
4 5 7
5 4 7
3 4 1
4 3 1
Saída: 
[[3, 4, 1], [2, 5, 2], [0, 1, 4], [2, 3, 6], [0, 4, 8]]

Exemplo2

Entrada:

9 28 0
0 1 4
1 0 4
0 8 8
8 0 8
1 8 11
8 1 11
1 2 8
2 1 8
2 3 7
3 2 7
2 5 4
5 2 4
2 7 2
7 2 2
3 4 9
4 3 9
3 5 14
5 3 14
4 5 10
5 4 10
5 6 2
6 5 2
6 7 6
7 6 6
6 8 1
8 6 1
7 8 7
8 7 7
Saída: 
[[6, 8, 1], [2, 7, 2], [5, 6, 2], [0, 1, 4], [2, 5, 4], [2, 3, 7], [0, 8, 8], [3, 4, 9]]