Descrição

Faça um programa que faz a leitura de um grafo e imprime os instantes de descoberta e de finialização para cada vértice do grafo, de acordo com uma visita DFS (ou busca em profundidade).



Entrada

Recebe n, m: n é o total de vértices, m o total de arcos (o vértice inicial sempre será o vértice 0).
A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime os instantes (descoberta e finalização) obtidos pela busca DFS.



Exemplo

Entrada:

6 8
0 1
0 3
1 4
2 4
2 5
3 1
4 3
5 5
Saída: 
[1, 2, 9, 4, 3, 10]
[8, 7, 12, 5, 6, 11]