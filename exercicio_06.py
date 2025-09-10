#int: é um tipo de dado que representa números inteiros, ou seja, números que não possuem parte decimal. É usado para armazenar números inteiros positivos, negativos ou zero. Além disso, a função int() é usada para converter valores para o tipo inteiro. 

numero=int(input("digite um numero inteiro:"))

#if: é uma estrutura de controle usada para iterar sobre uma sequência de números.
#else: é usado em conjunto com if para executar um bloco de código quando a condição do if for falsa. É uma estrutura condicional que permite definir um comportamento alternativo quando a condição principal não é atendida. 

#resto da divisão: o resto da divisão é obtido através do operador %, também conhecido como operador de módulo. Este operador retorna o resto da divisão inteira de um número pelo outro. Por exemplo, 7 % 3 resultaria em 1, pois 7 dividido por 3 tem resto 1. 
if numero % 2 == 0:
 print ("numero {numero} é par")

else:
 print("numero {numero} é impar")

#print: é uma função embutida usada para exibir informações na saída padrão, geralmente o console ou terminal.