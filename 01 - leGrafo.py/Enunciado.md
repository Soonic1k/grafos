Descrição

Faça um programa que faz a leitura de um grafo e imprime na tela as suas listas de adjacências.



Entrada

Recebe n e m; n é o total de vértices e m o total de arcos.
A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime as listas de adjacência.



Exemplo1

Entrada:

5 10
0 1
0 2
0 3
0 4
1 2
1 3
1 4
2 3
2 4
3 4
Saída: 

0: 1 2 3 4 
1: 2 3 4 
2: 3 4 
3: 4 
4: 


Exemplo2

Entrada:

6 14 1
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
0: 1 4
1: 0 2 4
2: 1 3
3: 2 4 5
4: 0 1 3
5: 3