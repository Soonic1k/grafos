Descrição

Faça um programa que faz a leitura de um grafo e imprime na tela as listas de adjacências do seu grafo transposto.



Entrada

Recebe n e m; n é o total de vértices e m o total de arcos.
A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
(Os vértices são identificados de 0 até n-1.)



Saída

Imprime as listas de adjacência do grafo transposto.



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

0: 
1: 0 3 
2: 
3: 0 4 
4: 1 2 
5: 2 5 