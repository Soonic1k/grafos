Descrição

Faça um programa que faz a leitura de um grafo e imprime a expressão de parênteses dos componentes fortemente conexos.



Entrada

Recebe n, m: n é o total de vértices, m o total de arcos.
A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime a expressão de parênteses dos componentes fortemente conexos.



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
(2 2) (5 5) (0 0) (1 (3 (4 4) 3) 1)