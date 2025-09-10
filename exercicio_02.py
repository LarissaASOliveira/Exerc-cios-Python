#float: é um tipo de dado que representa números de ponto flutuante, ou seja,casas decimais. float(input) = o programa pega o valor em texto e transforma em números decimais.

peso=float(input("digite o seu peso"))
altura=float(input("digite a sua altura"))

#Calculo de multiplicação: a multiplicação é realizada utilizando o operador *. Para multiplicar dois ou mais números, basta colocá-los entre o operador de multiplicação. Por exemplo, para multiplicar 5 por 3, você escreveria 5 * 3, e o resultado seria 15. 

imc = altura * altura/peso

#if: é uma estrutura de controle usada para iterar sobre uma sequência de números.
#elif é uma abreviação de "else if" e é usado para verificar várias condições em sequência após uma condição if inicial. Se a condição do if for falsa, o Python avalia a condição do elif.
#else: é usado em conjunto com if para executar um bloco de código quando a condição do if for falsa. É uma estrutura condicional que permite definir um comportamento alternativo quando a condição principal não é atendida. 

if imc<20.5:
    print("abaixo do peso")

elif imc <= 25 or imc< 30:
    print("peso normal")

elif imc<= 30 or imc< 35: 
    print("Sobre peso")

else:
    print("obesidade")

    print("seu imc é:") 