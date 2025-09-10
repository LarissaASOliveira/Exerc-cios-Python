#Variavel: é um nome que se refere a um valor que pode ser armazenado. 
#Para atribuir o valor na variável é necessário usar o sinal de igual (=).

Fahrenheit=float(input("insira a temperatura em Fahrenheit: "))

#float: é um tipo de dado que representa números de ponto flutuante, ou seja,casas decimais. float(input) = o programa pega o valor em texto e transforma em números decimais.
Celsius = (Fahrenheit - 32)  * 5/9

#print: é uma função embutida usada para exibir informações na saída padrão, geralmente o console ou terminal.
#format: utilizado para formatar ou personalizar strings, inserindo valores em espaços reservados dentro da string. Esses espaços reservados são delimitados por chaves {} e podem ser preenchidos com valores fornecidos como argumentos para o método format.

print ("A temperatura em celsius é:", format(Celsius, ".2f"))