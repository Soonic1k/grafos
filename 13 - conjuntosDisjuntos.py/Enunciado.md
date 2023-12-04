Descrição

Faça um programa que implemente as operações com Conjuntos Disjuntos e imprima os resultados correspondentes.



Entrada

Inicialmente, S é vazio.
A primeira linha contém n, o total de operações com S.
As linhas a seguir, temos n linhas, cada uma com uma operação:

- findSet (S, x): devolve um representante de S_x.
- makeSet (S, x): cria um novo conjunto com um único elemento x.
- union (S, x, y): une dois conjuntos S_x e S_y.

Saída

Imprime os resultados das operações com Conjuntos Disjuntos.
Após cada operação "makeSet" ou "union", imprima o S resultante.
Após cada operação "findSet" imprima o índice (representante) e S.



Exemplo

Entrada:

7
M a
M b
M c
F a
F b
F c
U b c
Saída: 
[['a']]
[['a'], ['b']]
[['a'], ['b'], ['c']]
0 [['a'], ['b'], ['c']]
1 [['a'], ['b'], ['c']]
2 [['a'], ['b'], ['c']]
[['a'], ['b', 'c'], []]