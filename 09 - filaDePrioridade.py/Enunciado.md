Descrição

Faça um programa que implemente uma fila de prioridade e imprima na tela os resultados das operações especificadas na entrada.



Entrada

Na primeira linha, o programa recebe dois inteiros n e k: n é o tamanho da fila, k é a quantidade de operações.
Inicialmente, a fila Q está vazia, ou seja, Q = [0] * n.
Na segunda linha, temos n chaves.
A partir da terceira linha, temos k operações, uma operação por linha.

Cada operação pode ser:

- vazio (Q): devolve True se fila vazia, False caso contrário.
- insere (Q, i): insere o índice i na fila Q, ou seja, faz Q[i] = 1.
- busca (Q, i): devolve 1 se o índice i estiver na fila, 0 caso contrário (ou seja, devolve Q[i]).
- extraiMinimo (Q): remove e devolve o índice de Q com a menor chave.
- minimo (Q): devolve o índice de Q com a menor chave (sem remover).


Saída

Imprime os resultados das operações com a fila de prioridade.
Após cada operação "insere", imprima a fila resultante.
Após "extraiMinimo", imprima o elemento removido e a fila resultante. 
Após "minimo", imprima o elemento devolvido e a fila resultante.
Após "busca" ou "vazio", imprima o resultado e a fila.



Exemplo

Entrada:

5 10
10 20 12 30 14
I 2
I 1
I 4
M
E
B 2
V
E
E
V

Saída: 

[0, 0, 1, 0, 0]
[0, 1, 1, 0, 0]
[0, 1, 1, 0, 1]
2 12 [0, 1, 1, 0, 1]
2 12 [0, 1, 0, 0, 1]
0 [0, 1, 0, 0, 1]
False [0, 1, 0, 0, 1]
4 14 [0, 1, 0, 0, 0]
1 20 [0, 0, 0, 0, 0]
True [0, 0, 0, 0, 0]