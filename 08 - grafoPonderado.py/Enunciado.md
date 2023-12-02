Descrição

Faça um programa que faz a leitura de um grafo ponderado e imprime na tela as suas listas de adjacências com os pesos de cada arco.



Entrada

Recebe n e m; n é o total de vértices e m o total de arcos.
A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime as listas de adjacência com os pesos.



Exemplo

Entrada:

6 8
0 1 10
0 3 15
1 4 12
2 4 20
2 5 25
3 1 13
4 3 16
5 5 11
Saída: 

0: 1(10) 3(15) 
1: 4(12) 
2: 4(20) 5(25) 
3: 1(13) 
4: 3(16) 
5: 5(11)